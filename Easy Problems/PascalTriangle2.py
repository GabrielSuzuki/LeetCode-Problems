class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        endArr = [[1],[1,1]]
        tempArr = []
        for i in range(1,rowIndex):
            tempArr = [1]
            for j in range(0,len(endArr[-1])-1):
                tempArr.append(endArr[-1][j]+endArr[-1][j+1])
            tempArr.append(1)
            endArr.append(tempArr)
        return endArr[-1]