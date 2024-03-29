func findDuplicates(nums []int) []int {
	output := int[]{}
	seen := make(map[int]bool)
	for _, num := nums {
		if seen[num] {
			output = append(output, num)
		}
		seen[num] = true
	}
	return output
}