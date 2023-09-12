class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        #using a inbuilt function to split
        x = s.split()
        return len(x[len(x)-1])

        #Split manually 
        # x = []
        # j = flag1 = flag2 = 0
        
        # for i in s:
        #     if i != " ":
        #         if(len(x) == j):
        #             x.append(i)
        #         else:
        #             x[j] = x[j] + i
        #         flag1 = 0
        #         flag2 = 1
        #     else:
        #         if flag2 == 1:                    
        #             j += 1
        #             flag1 = 1
        #             flag2 = 0

        # if(flag1 == 0):
        #     return len(x[j])
        # else:
        #     return len(x[j-1])