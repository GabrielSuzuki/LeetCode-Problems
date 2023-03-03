class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        curr = 0
        n = len(s)
        if s == "":
            return True
        for i in range(0,len(s)):
            for j in range(curr,len(t)):
                if s[i] == t[j]:
                    count += 1
                    if count == n:
                        return True
                    curr += 1
                    break
                curr += 1
        return False