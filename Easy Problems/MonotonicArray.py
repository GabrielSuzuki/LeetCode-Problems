class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        inc = True
        setInc = False
        for i in range(1,len(nums)):
            print(nums[i],inc)
            if nums[i-1] < nums[i]:
                if not setInc:
                    inc = True
                    setInc = True
                if not inc:
                    return False
            elif nums[i-1] > nums[i]:
                if not setInc:
                    inc = False
                    setInc = True
                if inc:
                    return False
        return True