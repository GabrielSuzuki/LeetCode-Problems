class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s)-1
        while i < j:
            if s[i].isalpha() == False:
                i += 1
                continue
            if s[j].isalpha() == False:
                j -= 1
                continue
            temp = s[j]
            s = s[:j] + s[i] + s[j+1:]
            s = s[:i] + temp + s[i+1:]
            i += 1
            j -= 1
        return s