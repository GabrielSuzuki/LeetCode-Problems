class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        newArr = []
        output = []
        for i in range(0,len(mat)):
            newArr.append([sum(mat[i]),i])
        newArr = sorted(newArr)
        for i in range(k):
            output.append(newArr[i][1])
        return output