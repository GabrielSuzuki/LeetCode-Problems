import itertools
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        for j in range(0,len(nums)+1):
            for i in combinations(nums,j):
                if sorted(i) not in output:
                    output.append(sorted(i))
        return output