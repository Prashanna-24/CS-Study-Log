package main

import (
	"fmt"
	"net/rpc"
	"sync"
)

type Request struct {
	Roomtype int
}

type Response struct {
	Answer    string
	Timestamp string
}

func bookRoom(wg *sync.WaitGroup, roomType int) {
	defer wg.Done()

	client, err := rpc.Dial("tcp", ":1234")
	if err != nil {
		fmt.Println("ERROR rpc.Dial()")
		return
	}
	defer client.Close()

	req := Request{Roomtype: roomType}
	var res Response

	err = client.Call("Hotel.BookRoom", req, &res)
	if err != nil {
		fmt.Println("error occurred")
		return
	}
	fmt.Printf("Room Type: %d | Response: %s | Timestamp: %s\n", roomType, res.Answer, res.Timestamp)
}

func main() {
	var wg sync.WaitGroup
	numClients := 10 // Number of concurrent requests

	for i := 0; i < numClients; i++ {
		wg.Add(1)
		go bookRoom(&wg, i%4) // Rotate between room types (0-3)
	}

	wg.Wait()
}
