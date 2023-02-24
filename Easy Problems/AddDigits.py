class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = 0
        while num > 9:
            temp = 0
            for i in str(num):
                temp += int(i)
            num = temp
        return num 