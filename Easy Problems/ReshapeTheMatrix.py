class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat) * len(mat[0]) != r * c:
            return mat
        tempList = []
        outputList = [[] for row in range(r)]
        for i in mat:
            tempList += i
        colCount = 0
        rowCount = 0
        for i in range(0,len(tempList)):
            outputList[rowCount].append(tempList[i])
            colCount += 1
            if colCount == c:
                colCount = 0
                rowCount += 1    
        return outputList