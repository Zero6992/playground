func findDuplicates(nums []int) []int {
	output := []int{}
	for _, num := range nums {
		index := 0
		// abs, minus one because nums are in the range [1, n]
		if num < 0 {
			index = -num - 1
		} else {
			index = num - 1
		}
		// check if the asme index in nums had been changed before, plus one to the real duplicate numbers
		if nums[index] < 0 {
			output = append(output, index+1)
		}
		nums[index] = -nums[index]
	}

	return output
}