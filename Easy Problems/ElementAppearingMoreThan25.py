class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        fourth = len(arr) // 4
        intDict = {}
        for i in arr:
            if i not in intDict:
                intDict[i] = 1
            else:
                intDict[i] += 1
                if intDict[i] > fourth:
                    return i
        return arr[0]