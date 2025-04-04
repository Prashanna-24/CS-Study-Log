package main

import (
	"fmt"
)

func sumWorker(nums []int, ch chan int) {
	sum := 0
	for _, n := range nums {
		sum += n
	}
	ch <- sum
}

func main() {
	arr := [10]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	numbers := arr[:] // convert to slice for ease of use
	ch := make(chan int, 2)

	mid := len(numbers) / 2
	go sumWorker(numbers[:mid], ch)
	go sumWorker(numbers[mid:], ch)

	sum1 := <-ch
	sum2 := <-ch
	fmt.Println(sum1 + sum2)
}
