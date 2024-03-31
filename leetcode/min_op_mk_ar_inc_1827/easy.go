func minOperations(nums []int) int {
	if len(nums) == 1 {
		return 0
	}
	output, currentMax := 0, 0
	for _, num := range nums {
		if num > currentMax {
			currentMax = num
		} else {
			currentMax++
			output += (currentMax - num)
		}
	}
	return output
}