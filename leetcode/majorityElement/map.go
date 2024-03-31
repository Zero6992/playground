func majorityElement(nums []int) int {
	seen := make(map[int]int)
	for _, num := range nums {
		if seen[num] > 0 {
			seen[num]++
		} else {
			seen[num] = 1
		}

	}
	maxValue, maxIndex := 0, 0
	for index, value := range seen {
		if value > maxValue {
			maxValue = value
			maxIndex = index
		}
	}
	return maxIndex
}