func convert(s string, numRows int) string {

	if numRows == 1 {
		return s
	}

	temp := make([]string, numRows)
	result := ""
	row := 0
	nextMove := -1

	for i := 0; i < len(s); i++ {
		if row == 0 || row == numRows-1 {
			nextMove *= -1
		}

		temp[row] += string(s[i])

		row += nextMove
	}

	for _, value := range temp {
		result += value
	}

	return result

}