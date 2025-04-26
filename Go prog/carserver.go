package main

import (
	"fmt"
	"net"
	"net/rpc"
	"sync"
)

type Request struct {
	CarType string
}

type Response struct {
	Msg string
}

type Cars struct {
	mu        sync.Mutex
	count_map map[string]int
}

func (c *Cars) RentCar(req Request, res *Response) error {
	c.mu.Lock()
	defer c.mu.Unlock()

	count, exists := c.count_map[req.CarType]

	if !exists {
		res.Msg = "invalid cartype"
	} else if count > 0 {
		c.count_map[req.CarType]--
		res.Msg = fmt.Sprintf("car rented successfully! \n Remaining: %d", c.count_map[req.CarType])
	} else {
		res.Msg = "car not available"
	}

	return nil
}

func main() {
	cars_db := &Cars{
		count_map: map[string]int{"E": 10, "S": 15, "SU": 5, "L": 6},
	}
	err := rpc.Register(cars_db)
	if err != nil {
		fmt.Println("rpc.Register(cars_db) ERROR")
		return
	}

	listener, err := net.Listen("tcp", ":1234")
	if err != nil {
		fmt.Println("net.Listen() ERROR")
		return
	}
	defer listener.Close()
	fmt.Println("server listening")

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("listener.Accept() ERROR")
			return
		}
		go rpc.ServeConn(conn)
	}
}
