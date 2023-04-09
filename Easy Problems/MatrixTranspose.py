class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        newMatrix = [[]for _ in range(len(matrix[0]))]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                newMatrix[j].append(matrix[i][j])
        return newMatrix