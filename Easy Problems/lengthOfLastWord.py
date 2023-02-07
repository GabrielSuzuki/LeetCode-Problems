class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        count = 0
        while s[i] == " ":
            i -= 1
        while s[i] != " ":
            i -= 1
            count += 1
            if i == -1:
                return count
        return count