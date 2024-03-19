package main

import (
	"fmt"

	"tiotimothy.com/algorithm/code"
)

func main() {
	array := []int{1, 2, 3, 20, 10, 9, 100}
	code.MergeSort(array, 0, len(array)-1)
	fmt.Println(array)

	array = []int{1, 2, 3, 20, 10, 9, 100}
	code.QuickSort(array, 0, len(array)-1)
	fmt.Println(array)
}
