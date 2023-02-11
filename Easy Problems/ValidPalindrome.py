class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sTemp = ""
        for i in s:
            if i.isalpha():
                sTemp += i.lower()
            if i.isdigit():
                sTemp += i
        j = 0
        while j < len(sTemp)/2:
            if sTemp[j] != sTemp[len(sTemp)-j-1]:
                return False
            j += 1
        return True