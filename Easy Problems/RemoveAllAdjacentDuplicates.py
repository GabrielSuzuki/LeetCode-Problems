class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0 
        n = len(s)-1
        while i < n:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                n -= 2
                if i > 0:
                    i -= 1
            else:
                i += 1
        return s