package main

import (
	"fmt"

	"example.com/ttiimmothy/pseudocode/code"
)

func main() {
	array := []int{1, 2, 3}
	code.MergeSort(array, 0, len(array)-1)
	code.QuickSort(array, 0, len(array)-1)
	fmt.Println(array)
}
