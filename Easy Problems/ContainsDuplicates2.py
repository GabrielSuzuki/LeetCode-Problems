class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numDict = {}
        for i in range(0,len(nums)):   
            if numDict.get(nums[i]) == None or abs(numDict.get(nums[i])-i) > k:
                numDict[nums[i]] = i
            else:
                return True
        return False 