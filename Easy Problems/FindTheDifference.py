class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
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
        first = list(firstDict.keys())
        for i in list(secondDict.keys()):
            if i not in first:
                return i
            if firstDict[i] != secondDict[i]:
                return i
        return ""