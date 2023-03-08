from itertools import permutations
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tempArr = []
        for i in permutations(nums):
            if i not in tempArr:
                tempArr.append(i)
        return tempArr