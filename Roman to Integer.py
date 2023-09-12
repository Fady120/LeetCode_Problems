class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        intgers = []
        final = [] 

        flagAdd = 0
        i = 0

        for roman in s:
            if(roman == 'I'):
                intgers.append(1)
            elif(roman == 'V'):
                intgers.append(5)
            elif(roman == 'X'):
                intgers.append(10)
            elif(roman == 'L'):
                intgers.append(50)
            elif(roman == 'C'):
                intgers.append(100)
            elif(roman == 'D'):
                intgers.append(500) 
            elif(roman == 'M'):
                intgers.append(1000) 

        while (i <= len(intgers)-2):
            if(intgers[i] < intgers[i+1]):
                subValue = intgers[i+1] - intgers[i]
                final.append(subValue)
                i += 1
                if(i >= len(intgers)-1):
                    flagAdd = 1
            else:
                final.append(intgers[i])
            i += 1

        if(flagAdd == 0):
            final.append(intgers[len(intgers)-1])
        
        return sum(final)
