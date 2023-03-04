class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphaDict = {}
        more = False
        count = 0
        for i in range(0,len(s)):
            if alphaDict.get(s[i]) == None:
                alphaDict[s[i]] = 1
            else:
                alphaDict[s[i]] += 1
        for i in list(alphaDict.values()):
            if i % 2 == 1:
                if more == False:
                    count += i
                else:
                    if i > 1:
                        count += i-1
                more = True
            else:
                count += i
        return count