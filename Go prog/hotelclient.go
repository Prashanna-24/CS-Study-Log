package main

import (
	"fmt"
	"net/rpc"
)

type Request struct {
	Roomtype int
}

type Response struct {
	Answer    string
	Timestamp string
}

func main() {
	client, err := rpc.Dial("tcp", ":1234")
	if err != nil {
		fmt.Println("ERROR rpc.Dial()")
		return
	}
	defer client.Close()
	req := Request{Roomtype: 1}
	var res Response

	err = client.Call("Hotel.BookRoom", req, &res)
	if err != nil {
		fmt.Println("error occured")
		return
	} else {
		fmt.Printf("Response: %s\nTimestamp: %s\n", res.Answer, res.Timestamp)
	}
}
