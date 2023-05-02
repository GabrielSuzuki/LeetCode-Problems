class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        output = 0
        expected = sorted(heights)
        for i in range(0,len(heights)):
            if expected[i] != heights[i]:
                output += 1
        return output