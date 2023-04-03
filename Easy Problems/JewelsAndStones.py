class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        tempArr = []
        for i in matrix:
            tempArr += i
        for i in range(0,len(tempArr)-len(matrix[0])-1):
            if (i + 1) % len(matrix[0]) == 0:
                continue
            if tempArr[i] != tempArr[i + len(matrix[0]) + 1]:
                return False
        return True