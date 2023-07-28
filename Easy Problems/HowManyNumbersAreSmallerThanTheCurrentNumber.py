class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newArr = []
        for i in nums:
            tempCount = 0
            for j in nums:
                if i > j:
                    tempCount += 1
            newArr.append(tempCount)
        return newArr