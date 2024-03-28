package main

import (
	"fmt"
	"sort"
)

func distributeElements(array []int) ([]int, []int) {
	sort.Sort(sort.Reverse(sort.IntSlice(array)))
	A, B := []int{}, []int{}
	sumA, sumB := 0, 0

	for _, value := range array {
		if sumA <= sumB {
			A = append(A, value)
			sumA += value
		} else {
			B = append(B, value)
			sumB += value
		}
	}

	return A, B
}

func main() {
	array := []int{3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 14}
	A, B := distributeElements(array)
	fmt.Println("A:", A, "Sum of A:", sum(A))
	fmt.Println("B:", B, "Sum of B:", sum(B))
}

func sum(nums []int) int {
	total := 0
	for _, num := range nums {
		total += num
	}
	return total
}
