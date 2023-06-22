class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        tempDict = {}
        j = 1
        output = []
        sortedList = sorted(arr)
        for i in sortedList:
            if i not in tempDict:
                tempDict[i] = j
                j += 1
        for i in arr:
            output.append(tempDict[i])
        return output 