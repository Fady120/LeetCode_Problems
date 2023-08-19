func lengthOfLongestSubstring(s string) int {

	s1 := []rune{}
	temp := []rune{}

	for _, value := range s {
		for index1, value1 := range s1 {
			if value == value1 {
				if temp == nil || len(temp) <= len(s1) {
					temp = s1
				}
				s1 = s1[index1+1:]
				continue
			}
		}
		s1 = append(s1, value)
	}

	if len(temp) <= len(s1) {
		return len(s1)
	} else {
		return len(temp)
	}

}