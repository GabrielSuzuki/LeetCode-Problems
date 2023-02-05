class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0,len(nums)):
            if target == nums[i]:
                return i
            elif i == 0 and nums[i] > target:
                return 0
            elif i == len(nums) -1 and nums[i] < target:
                return len(nums)
            elif nums[i] < target and nums[i+1] > target:
                return i+1 