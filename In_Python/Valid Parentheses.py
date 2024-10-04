class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        from collections import deque

        stack = deque()

        closedBrackets = [')','}',']']
        oponedBrackets = ['(','{','[']

        for bracket in s:
            flag = 0
            for closed in closedBrackets:
                if(bracket == closed):
                    flag = 1
                    if(bool(stack) == False):
                        return False
                    second = stack.pop()
                    index = closedBrackets.index(bracket)
                    if(second != oponedBrackets[index]):
                        return False
            if(flag == 0):
                stack.append(bracket)
        if(bool(stack) == True):
            return False
        if(flag == 1):
            return True
                
