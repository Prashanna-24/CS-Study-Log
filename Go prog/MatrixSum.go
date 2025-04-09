package main

import (
	"fmt"
)

func addRows(row1 []int, row2 []int, ch chan []int) {
	row_sum := make([]int, len(row1))
	for i, n1 := range row1 {
		row_sum[i] = n1 + row2[i]
	}
	ch <- row_sum
}

func main() {
	mat1 := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	mat2 := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}

	ch := make(chan []int)
	result_arr := make([][]int, len(mat1))

	for i := 0; i < 3; i++ {
		go addRows(mat1[i], mat2[i], ch)
		result_arr[i] = <-ch
	}
	fmt.Println(result_arr)
}
