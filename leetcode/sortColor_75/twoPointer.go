func sortColors(nums []int) {
	const RED, WHITE, BLUE = 0, 1, 2
	index_red, index_blue := 0, len(nums) - 1
	for i := 0; i <= index_blue ; i++ {
		if nums[i] == RED {
			nums[i], nums[index_red] = nums[index_red], nums[i]
			index_red++
		} else if nums[i] == BLUE {
			nums[i], nums[index_blue] = nums[index_blue], nums[i]
			index_blue--
			i--
		}
	}
	return
}