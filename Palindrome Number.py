class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x_reverse = "".join(reversed(str(x)))

        if (x_reverse == str(x)):
            return True
        else:
            return False
        
