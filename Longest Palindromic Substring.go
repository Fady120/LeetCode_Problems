func longestPalindrome(s string) string {

	end, start := 0, 0
	l := len(s)

	for i := 0; i < l; i++ {
		n, startTemp := i, i
		endTemp := 0
		for j := l - 1; j >= i; j-- {
			if n == i {
				endTemp = j
			}
			if s[j] != s[n] && n != i {
				j = endTemp
				n = i
			} else if i != j {
				n++
			}
		}
		if endTemp-startTemp > end-start {
			start = startTemp
			end = endTemp
		}

	}

	return s[start : end+1]

}