class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rowDict = []
        for i in range(0,len(matrix)):
            for j in matrix[i]:
                if j == 0:
                    rowDict.append(i)
                    break
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j] == 0:
                    for k in range(0,len(matrix)):
                        matrix[k][j] = 0
        for i in rowDict:
            matrix[i] = [0]*len(matrix[0])