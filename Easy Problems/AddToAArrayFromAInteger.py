class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        number = ""
        for i in num:
            number += str(i)
        temp = str(int(number)+k)
        output = []
        for i in range(0,len(temp)):
            output.append(int(temp[i]))
        return output