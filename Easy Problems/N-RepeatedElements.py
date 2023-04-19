class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = {}
        for i in nums:
            if i not in numDict:
                numDict[i] = 1
            else:
                return i