func isPalindrome(x int) bool {
	string := strconv.Itoa(x)
	l := len(string)
	for i := 0; i < l; i++ {
		if string[i] != string[l-1-i] {
			return false
		}
	}
	return true
}