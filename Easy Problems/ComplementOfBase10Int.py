class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        newN = str(bin(n))[2:]
        newStr = ""
        for i in range(0,len(newN)):
            if newN[i] == '0':
                newStr += '1'
            else:
                newStr += '0'
        return int("0b"+newStr,2)