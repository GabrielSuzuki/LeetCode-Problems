class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numDict = {}
        for i in nums:
            if numDict.get(i) == None:
                numDict[i] = 1
            else:
                return True
        return False