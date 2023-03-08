class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        str1 = str(bin(x))[2:]
        str2 = str(bin(y))[2:]
        count = 0
        least = len(str1)
        most = len(str2)
        mostStr = 0
        if len(str1) < len(str2):
            least = len(str1)
            most = len(str2)
            mostStr = str2
        elif len(str2) < len(str1):
            least = len(str2)
            most = len(str1)
            mostStr = str1
        for i in range(1,most+1):
            if i <= least:
                if str2[-i] != str1[-i]:
                    count += 1
            else:
                if mostStr[-i] == '1':
                    count += 1
        return count