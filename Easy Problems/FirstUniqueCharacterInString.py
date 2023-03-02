class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphaDict = {}
        for i in range(0,len(s)):
            if alphaDict.get(s[i]) == None:
                alphaDict[s[i]] = 1
            else:
                alphaDict[s[i]] += 1
        for i in range(0,len(s)):
            if alphaDict[s[i]] == 1:
                return i
        return -1