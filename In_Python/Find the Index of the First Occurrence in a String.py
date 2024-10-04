class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        h = len(haystack)
        n = len(needle)

        # Catch 
        for i in range(h-n+1):
            for j in range(n):
                if needle[j] != haystack[i+j]:
                    break
                if j == n-1:
                    return i
        
        return -1