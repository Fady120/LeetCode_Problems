class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        
        romanDec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0

        s = s.replace("IV", "IIII").replace("IX", "VIIII") \
             .replace("XL", "XXXX").replace("XC", "LXXXX") \
             .replace("CD", "CCCC").replace("CM", "DCCCC")

        for i in s:
            total += romanDec[i]

        return total