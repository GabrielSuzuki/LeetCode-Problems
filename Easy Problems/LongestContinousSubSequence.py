class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        overallCount = 0
        if len(nums) == 1:
            return 1
        for i in range(0,len(nums)-1):
            count = 1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[j-1]:
                    count += 1
                else:
                    break
            overallCount = max(overallCount,count)
            if overallCount >= len(nums) - i:
                return overallCount
        return overallCount