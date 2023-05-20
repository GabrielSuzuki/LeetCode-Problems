class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = str(n)
        product = 1
        sumNum = 0
        for i in range(len(temp)):
            product *= int(temp[i])
            sumNum += int(temp[i])
        return product - sumNum