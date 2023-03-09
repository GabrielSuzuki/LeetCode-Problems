class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        output = ""
        temp = str(bin(num))[2:]
        for i in range(0,len(temp)):
            if temp[i] == '1':
                output += '0'
            else:
                output += '1'
        return int(output,2)