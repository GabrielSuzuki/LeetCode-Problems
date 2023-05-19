class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        rTotal = 0
        lTotal = 0
        output = 0
        for i in range(len(s)):
            if s[i] == "R":
                rTotal += 1
            if s[i] == "L":
                lTotal += 1
            if lTotal == rTotal:
                lTotal = 0
                rTotal = 0
                output += 1
        return output