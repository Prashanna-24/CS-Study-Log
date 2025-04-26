// server.go
package main

import (
	"fmt"
	"net"
	"net/rpc"
	"sort"
	"sync"
	"time"
)

type Request struct {
	Roomtype int
}

type AddRoomRequest struct {
	Roomtype int
	Count    int
	Price    int
}

type Response struct {
	Answer    string
	Timestamp string
}

type Room struct {
	AvailableCount int
	Price          int
}

type Hotel struct {
	mu    sync.Mutex
	Rooms map[int]*Room
}

func (h *Hotel) BookRoom(req Request, res *Response) error {
	h.mu.Lock()
	defer h.mu.Unlock()

	room, exists := h.Rooms[req.Roomtype]
	if !exists {
		res.Answer = "Invalid room type."
	} else if room.AvailableCount > 0 {
		room.AvailableCount--
		res.Answer = "Room booked successfully!"
	} else {
		res.Answer = "Room not available."
	}
	res.Timestamp = time.Now().Format(time.RFC3339)
	return nil
}

func (h *Hotel) AddRoom(req AddRoomRequest, res *Response) error {
	h.mu.Lock()
	defer h.mu.Unlock()

	if _, exists := h.Rooms[req.Roomtype]; exists {
		res.Answer = "Room type already exists."
	} else {
		h.Rooms[req.Roomtype] = &Room{AvailableCount: req.Count, Price: req.Price}
		res.Answer = "Room added successfully!"
	}
	res.Timestamp = time.Now().Format(time.RFC3339)
	return nil
}

func (h *Hotel) DeleteRoom(req Request, res *Response) error {
	h.mu.Lock()
	defer h.mu.Unlock()

	if _, exists := h.Rooms[req.Roomtype]; exists {
		delete(h.Rooms, req.Roomtype)
		res.Answer = "Room type deleted successfully!"
	} else {
		res.Answer = "Room type does not exist."
	}
	res.Timestamp = time.Now().Format(time.RFC3339)
	return nil
}

type SortedRoomsResponse struct {
	Rooms     []Room
	Timestamp string
}

func (h *Hotel) GetRoomsSorted(_ struct{}, res *SortedRoomsResponse) error {
	h.mu.Lock()
	defer h.mu.Unlock()

	var rooms []Room
	for _, room := range h.Rooms {
		rooms = append(rooms, *room)
	}

	sort.Slice(rooms, func(i, j int) bool {
		return rooms[i].AvailableCount > rooms[j].AvailableCount
	})

	res.Rooms = rooms
	res.Timestamp = time.Now().Format(time.RFC3339)
	return nil
}

func main() {
	myHotel := &Hotel{
		Rooms: map[int]*Room{
			0: {AvailableCount: 10, Price: 1000},
			1: {AvailableCount: 20, Price: 1500},
			2: {AvailableCount: 5, Price: 2000},
			3: {AvailableCount: 3, Price: 3000},
		},
	}
	err := rpc.Register(myHotel)
	if err != nil {
		fmt.Println("ERROR: rpc.Register(myHotel)")
		return
	}

	listener, err := net.Listen("tcp", ":1234")
	if err != nil {
		fmt.Println("ERROR: net.Listen()")
		return
	}
	defer listener.Close()
	fmt.Println("Server listening on port 1234...")

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("ERROR: listener.Accept()")
			continue
		}

		go rpc.ServeConn(conn)
	}
}
