class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        stringNum = "0b"
        output = []
        for i in nums:
            stringNum += str(i)
            testNum = int(stringNum,2)
            if testNum % 5 == 0:
                output.append(True)
            else:
                output.append(False)
        return output