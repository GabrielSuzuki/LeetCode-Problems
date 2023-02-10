class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        endArr = [[1],[1,1]]
        tempArr = []
        for i in range(2,numRows):
            tempArr = [1]
            for j in range(0,len(endArr[-1])-1):
                tempArr.append(endArr[-1][j]+endArr[-1][j+1])
            tempArr.append(1)
            endArr.append(tempArr)
        return endArr