package main

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for index, value := range nums {
		remaining := target - value
		if _, ok := m[remaining]; ok {
			return []int{m[remaining], index}
		}
		m[value] = index
	}
	return nil
}
