class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        output = str(bin(int(a,2)+int(b,2)))
        return output[2:]