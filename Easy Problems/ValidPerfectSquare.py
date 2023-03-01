class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sqrt = float(num) ** (1.0/2.0)
        if float(num) % sqrt != 0:
            return False
        else:
            return True