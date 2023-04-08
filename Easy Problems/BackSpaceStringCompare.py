class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sStack = []
        tStack = []
        for i in range(0,len(s)):
            if s[i] != "#":
                sStack.append(s[i])
            elif sStack != []:
                sStack.pop()
        for j in range(0,len(t)):
            if t[j] != "#":
                tStack.append(t[j])
            elif tStack != []:
                tStack.pop()
        if sStack == tStack:
            return True
        else:
            return False