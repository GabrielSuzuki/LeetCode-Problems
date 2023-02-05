class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = nums[0]
        place = 0
        for i in range(1,len(nums)):
            
            if current != nums[i]:
                nums[place] = current
                current = nums[i]
                place += 1
        nums[place] = current
        return (place+1)