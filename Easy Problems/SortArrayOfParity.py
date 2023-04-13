class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evenArr = []
        oddArr = []
        output = []
        for i in nums:
            if i == 0:
                output.append(i)
            elif i % 2 == 0:
                evenArr.append(i)
            else:
                oddArr.append(i)
        return output+evenArr+oddArr