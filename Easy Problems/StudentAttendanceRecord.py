class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lCount = 0
        aCount = 0
        for i in range(0,len(s)):
            if s[i] == 'A':
                aCount += 1
                if aCount == 2:
                    return False
                lCount = 0
            elif s[i] == 'L':
                lCount += 1
                if lCount == 3:
                    return False
            else:
                lCount = 0
        return True