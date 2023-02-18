class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alphaDict = {}
        alphaDict2 = {}
        for i in range(0,len(s)):
            if alphaDict.get(s[i]) == None:
                alphaDict[s[i]] = t[i]
            else:
                if alphaDict[s[i]] != t[i]:
                    return False
            if alphaDict2.get(t[i]) == None:
                alphaDict2[t[i]] = s[i]
            else:
                if alphaDict2[t[i]] != s[i]:
                    return False
        return True