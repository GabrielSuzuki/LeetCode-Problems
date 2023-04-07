class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        start = 0
        end = 1
        output = []
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                if end - start >= 3:
                    output.append([start,end-1])
                start = i
                end = i + 1
            else:
                end += 1
        if end - start >= 3:
            output.append([start,end-1])
        return output