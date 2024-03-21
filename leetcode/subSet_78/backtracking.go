package main

func subsets(num []int) [][]int {
	output := [][]int{{}}
	for _, num := range nums {
		newSubsets := make([][]int, 0)
		for _, curr := range output {
			subset := make([]int, len(curr)+1)
			copy(subset, curr)
			subset[len(curr)] = num
			newSubsets = append(newSubsets, subset)
		}
		output = append(output, newSubsets...)
	}
	return output
}
