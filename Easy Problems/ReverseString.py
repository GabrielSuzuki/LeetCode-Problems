class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(0,len(s)/2):
            temp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = temp