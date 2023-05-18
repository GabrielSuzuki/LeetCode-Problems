class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arrDict = {}
        tempArr = []
        for i in arr:
            if i not in arrDict:
                arrDict[i] = 1
            else:
                arrDict[i] += 1
        for i in arrDict:
            if arrDict[i] in tempArr:
                return False
            tempArr.append(arrDict[i])
        return True