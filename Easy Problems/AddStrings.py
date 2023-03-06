class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        numDict = {
            "0" : 0,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9
        }
        mult = 1
        curr1 = 0
        curr2 = 0
        for i in range(len(num1)-1,-1,-1):
            curr1 += numDict[num1[i]] * mult
            mult *= 10
        mult = 1
        for i in range(len(num2)-1,-1,-1):
            curr2 += numDict[num2[i]] * mult
            mult *= 10
        return str(curr1+curr2)