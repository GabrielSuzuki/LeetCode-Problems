class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        y = ""
        if not x[0].isdigit():
            y += x[0]
            x = x[1:]
        if len(x) == 1:
            return int(x)
        while x[-1] == '0':
            x = x[:-1]
        

        i = len(x)-1
        while i > -1:
            y += x[i]
            i -= 1
        if int(y) < (-1*(2 ** 31)):
            return 0 
        if int(y) > (2**31-1):
            return 0
        return int(y)
        #    i -= 1

