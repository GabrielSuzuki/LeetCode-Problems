class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        firstDict = {}
        secondDict = {}
        for i in range(0,len(s)):
            if firstDict.get(s[i]) == None:
                firstDict[s[i]] = 1
            else:
                firstDict[s[i]] += 1
        for i in range(0,len(t)):
            if secondDict.get(t[i]) == None:
                secondDict[t[i]] = 1
            else:
                secondDict[t[i]] += 1
        if firstDict == secondDict:
            return True
        else:
            return False