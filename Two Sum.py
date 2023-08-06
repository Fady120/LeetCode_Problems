class Solution(object):
    def twoSum(self, nums, target):
        # current = 0
        def find(current):
            i = current + 1
            while(i < len(nums)):
                if(nums[current] + nums[i] == target):
                    output = {current, i}
                    return output
                else:
                    i = i + 1
            return find(current + 1)

        return find(0)
    
