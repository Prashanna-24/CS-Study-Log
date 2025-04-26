package main

import (
	"fmt"
	"net/rpc"
)

type Request struct {
	CarType string
}

type Response struct {
	Msg string
}

func main() {
	client, err := rpc.Dial("tcp", ":1234")
	if err != nil {
		fmt.Println("rpc.Dial() ERROR")
		return
	}
	defer client.Close()

	req := Request{CarType: "E"}
	var res Response

	err = client.Call("Cars.RentCar", req, &res)
	if err == nil {
		fmt.Printf("Response: %s", res.Msg)
	}
}
