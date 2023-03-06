class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempDict = {}

        for i in range(0,len(nums)):
            if tempDict.get(nums[i]) == None:
                tempDict[nums[i]] = 1
        nums = sorted(list(tempDict.keys()),reverse = True)
        for i in range(0,len(nums)):
            if i == 0 and len(nums) == 1:
                return nums[i]        
            elif i == 1 and len(nums) == 2:
                return nums[i-1]
            elif i == 2:
                return nums[i]
        return ans