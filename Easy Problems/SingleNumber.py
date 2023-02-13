class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = {}
        for i in nums:
            if numDict.get(i) != None:
                numDict[i] += 1
            else:
                numDict[i] = 1
        for key in numDict:
            if numDict[key] == 1:
                return key