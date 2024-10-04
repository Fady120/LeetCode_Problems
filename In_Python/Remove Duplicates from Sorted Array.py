class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def checkDuplicates(index):
            i = 0
            while i <= len(nums)-1:
                if nums[i] == nums[index]:
                    if i != index:
                        nums.pop(i)
                        continue
                i += 1
            if(index == len(nums)-1):
                return 0
            else:
                return checkDuplicates(index+1)
        
        checkDuplicates(0)