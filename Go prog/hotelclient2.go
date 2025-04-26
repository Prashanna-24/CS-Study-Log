// client.go
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

func main() {
	client, err := rpc.Dial("tcp", ":1234")
	if err != nil {
		fmt.Println("ERROR: rpc.Dial()")
		return
	}
	defer client.Close()

	for {
		fmt.Println("\nHotel Management System")
		fmt.Println("1. Book a Room")
		fmt.Println("2. Add a New Room Type")
		fmt.Println("3. Delete a Room Type")
		fmt.Println("4. View Sorted Room Database")
		fmt.Println("5. Exit")
		fmt.Print("Enter your choice: ")

		var choice int
		fmt.Scan(&choice)

		switch choice {
		case 1:
			var roomType int
			fmt.Print("Enter room type to book: ")
			fmt.Scan(&roomType)
			req := Request{Roomtype: roomType}
			var res Response

			err := client.Call("Hotel.BookRoom", req, &res)
			if err != nil {
				fmt.Println("Error:", err)
			} else {
				fmt.Printf("Response: %s\nTimestamp: %s\n", res.Answer, res.Timestamp)
			}

		case 2:
			var roomType, count, price int
			fmt.Print("Enter new room type ID: ")
			fmt.Scan(&roomType)
			fmt.Print("Enter room count: ")
			fmt.Scan(&count)
			fmt.Print("Enter room price: ")
			fmt.Scan(&price)
			req := AddRoomRequest{Roomtype: roomType, Count: count, Price: price}
			var res Response

			err := client.Call("Hotel.AddRoom", req, &res)
			if err != nil {
				fmt.Println("Error:", err)
			} else {
				fmt.Printf("Response: %s\nTimestamp: %s\n", res.Answer, res.Timestamp)
			}

		case 3:
			var roomType int
			fmt.Print("Enter room type to delete: ")
			fmt.Scan(&roomType)
			req := Request{Roomtype: roomType}
			var res Response

			err := client.Call("Hotel.DeleteRoom", req, &res)
			if err != nil {
				fmt.Println("Error:", err)
			} else {
				fmt.Printf("Response: %s\nTimestamp: %s\n", res.Answer, res.Timestamp)
			}

		case 4:
			var res SortedRoomsResponse
			err := client.Call("Hotel.GetRoomsSorted", struct{}{}, &res)
			if err != nil {
				fmt.Println("Error:", err)
			} else {
				fmt.Println("Sorted Room Database (By Availability):")
				for _, room := range res.Rooms {
					fmt.Printf("Available: %d | Price: %d\n", room.AvailableCount, room.Price)
				}
				fmt.Println("Timestamp:", res.Timestamp)
			}

		case 5:
			fmt.Println("Exiting...")
			os.Exit(0)

		default:
			fmt.Println("Invalid choice. Please enter a valid option.")
		}
	}
}
