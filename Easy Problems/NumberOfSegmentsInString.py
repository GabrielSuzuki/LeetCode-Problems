class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        if s.isspace():
            return 0
        n = 0
        for i in s.split(" "):
            if i != "":
                n += 1
        return n