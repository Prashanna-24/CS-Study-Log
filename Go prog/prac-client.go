package main

import (
	"fmt"
	"net/rpc"
	"os"
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

type SortedRoomsResponse struct {
	Rooms     []Room
	Timestamp string
}

func main(){
	client, err := rpc.Dial("tcp", ":1234")
	if err != nil {
		fmt.Println("ERROR: rpc.Dial()")
		return
	}
	defer client.Close()

	if
}