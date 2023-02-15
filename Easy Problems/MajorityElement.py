class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        numDict = {}
        if len(nums) == 1:
            return nums[0]
        for i in nums:
            if numDict.get(i) == None:
                numDict[i] = 1
            else:
                numDict[i] += 1
                if numDict[i] > n:
                    return i