class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        tempLetter = ""
        tempArray = ""
        minimum = len(strs[0])
        for i in range(1,len(strs)):
            minimum = min(minimum,len(strs[i]))
        for i in range(0,minimum):
            tempLetter = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != tempLetter:
                    return tempArray
            tempArray += tempLetter
        return tempArray