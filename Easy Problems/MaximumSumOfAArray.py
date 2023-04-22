class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        negCount = 0
        nums = sorted(nums)
        for i in nums:
            if i < 0:
                negCount += 1
        if negCount >= k:
            for i in range(k):
                nums[i] *= -1
            return sum(nums)
        else:
            for i in range(negCount):
                nums[i] *= -1
                k -= 1
        if k % 2 == 0:
            return sum(nums)
        else:
            nums = sorted(nums)
            nums[0] *= -1
            return sum(nums)