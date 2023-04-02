import itertools
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        for i in range(len(nums) + 1):
            output += list(combinations(nums,i))
        return output