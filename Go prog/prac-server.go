package main

import (
	"fmt"
	"net"
	"net/rpc"
	"sort"
	"sync"
)

type Request struct {
	Roomtype int
}

type Response struct {
	Answer string
}

type Addroomrequest struct {
	Roomtype int
	Count    int
	Price    int
}

type SortedRoomsResponse struct {
	Sortedrooms []Room
}

type Room struct {
	Availablecount int
	Price          int
}

type Hotel struct {
	mu    sync.Mutex
	Rooms map[int]*Room
}

func (h *Hotel) BookRoom(req Request, res *Response) error {
	h.mu.Lock()
	defer h.mu.Unlock()
	room1, exists := h.Rooms[req.Roomtype]
	if !exists {
		res.Answer = "Invalid room type."
	} else if room1.Availablecount > 0 {
		room1.Availablecount--
		res.Answer = "Room booked successfully!"
	} else {
		res.Answer = "Room not available."
	}

	return nil
}

func (h *Hotel) AddRoom(req Addroomrequest, res *Response) error {
	h.mu.Lock()
	defer h.mu.Unlock()

	_, exists := h.Rooms[req.Roomtype]
	if exists {
		res.Answer = "Room type already exists."
	} else {
		h.Rooms[req.Roomtype] = &Room{Availablecount: req.Count, Price: req.Price}
		res.Answer = "Room added successfully!"
	}

	return nil
}

func (h *Hotel) DeleteRoom(req Request, res *Response) error {
	h.mu.Lock()
	defer h.mu.Unlock()
	_, exists := h.Rooms[req.Roomtype]
	if exists {
		delete(h.Rooms, req.Roomtype)
		res.Answer = "Room type deleted."
	} else {
		res.Answer = "Room type does not exist."
	}

	return nil
}

func (h *Hotel) GetRoomsSorted(_ struct{}, res *SortedRoomsResponse) error {
	h.mu.Lock()
	defer h.mu.Unlock()
	var rooms4 []Room
	for _, temproom := range h.Rooms {
		rooms4 = append(rooms4, *temproom)
	}

	sort.Slice(rooms4, func(i, j int) bool {
		return rooms4[i].Availablecount > rooms4[j].Availablecount
	})

	res.Sortedrooms = rooms4

	return nil
}

func main() {
	myHotel := &Hotel{
		Rooms: map[int]*Room{
			0: {Availablecount: 10, Price: 1000},
			1: {Availablecount: 20, Price: 1500},
			2: {Availablecount: 5, Price: 2000},
			3: {Availablecount: 3, Price: 3000},
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
