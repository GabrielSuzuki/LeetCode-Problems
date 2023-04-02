class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedNums = sorted(nums)
        if sortedNums[-1] >= sortedNums[-2] * 2:
            for i in range(0,len(nums)):
                if nums[i] == sortedNums[-1]:
                    return i
        return -1