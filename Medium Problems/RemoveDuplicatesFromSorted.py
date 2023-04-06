class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        intDict = {}
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] in intDict:
                intDict[nums[i]] += 1
                if intDict[nums[i]] > 2:
                    nums.pop(i)
                    i -= 1
                    n -= 1
            else:
                intDict[nums[i]] = 1
            i += 1
        return len(nums)