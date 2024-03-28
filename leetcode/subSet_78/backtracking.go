package main

func subsets(nums []int) [][]int {
	output := [][]int{{}}
	for _, num := range nums {
		newSubsets := [][]int{}
		for _, curr := range output {
			newSubset := append([]int{}, curr...)
			newSubset = append(newSubset, num)
			newSubsets = append(newSubsets, newSubset)
		}
		output = append(output, newSubsets...)
	}
	return output
}
