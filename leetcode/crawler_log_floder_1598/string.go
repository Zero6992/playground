func minOperations(logs []string) int {
	result := 0
	for _, log := range logs {
		if log == "../" && result <= 0 || log == "./" {
			continue
		}
		if log == "../" {
			result--
		} else {
			result++
		}
	}
	return result
}