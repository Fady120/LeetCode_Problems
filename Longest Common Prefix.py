class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def compare(strs, first_strs, char, LCP):
            for value in strs[1:]:
                if( char < len(value) and char < len(first_strs) ):
                    if(first_strs[char] != value[char]):
                        return LCP
                else: 
                    return LCP
            LCP += first_strs[char]
            char += 1
            return compare(strs, first_strs, char, LCP)
        if(len(strs) == 1):
            return strs[0]
        else:
            return compare(strs, strs[0], 0, '')
        
