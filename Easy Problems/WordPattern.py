class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        sSplit = []
        sSplit = s.split(" ")
        wordDict = {}
        if len(pattern) != len(sSplit):
            return False
        for i in range(0,len(sSplit)):
            if wordDict.get(pattern[i]) == None:
                for j in list(wordDict.values()):
                    if j == sSplit[i]:
                        return False
                wordDict[pattern[i]] = sSplit[i]
            else:
                if wordDict[pattern[i]] != sSplit[i]:
                    return False
        return True