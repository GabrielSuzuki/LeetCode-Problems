class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 2 4 16 37 58 89 145 42 20
        inputStr = str(n)
        subtotal = 0
        savedDict = { n:"met"}
        while inputStr != "1":
            subtotal = 0
            for i in inputStr:
                subtotal += int(i)**2
            if savedDict.get(subtotal) == "met":
                return False
            else:
                savedDict[subtotal] = "met"
            inputStr = str(subtotal)
        return True