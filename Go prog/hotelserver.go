package main

import (
	"fmt"
	"net"
	"net/rpc"
	"sync"
	"time"
)

type Request struct {
	Roomtype int
}

type Response struct {
	Answer    string
	Timestamp string
}

type Room struct {
	Availabecount int
	Price         int
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
		res.Answer = "invalid room type no"
	} else if room.Availabecount > 0 {
		room.Availabecount--
		res.Answer = "Room booked successbulee!"
	} else {
		res.Answer = "room not availbe"
	}
	res.Timestamp = time.Now().Format(time.RFC3339)

	return nil
}

func main() {
	myhotel := &Hotel{
		Rooms: map[int]*Room{
			0: {Availabecount: 10, Price: 1000},
			1: {Availabecount: 20, Price: 1500},
			2: {Availabecount: 5, Price: 2000},
			3: {Availabecount: 3, Price: 3000},
		},
	}
	err := rpc.Register(myhotel)
	if err != nil {
		fmt.Println("ERROR rpc.Register(myhotel)")
		return
	}

	listener, err := net.Listen("tcp", ":1234")
	if err != nil {
		fmt.Println("ERROR net.Listen()")
		return
	}
	defer listener.Close()
	fmt.Print("server listening")

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("ERROR listener.Accept()")
			return
		}

		go rpc.ServeConn(conn)
	}

}
