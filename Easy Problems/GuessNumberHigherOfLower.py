# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1 
        base = 1
        top = n

        while base != top:
            curr = guess((top-base)/2+base)
            if curr != 0 and top-base == 1:
                return top
            if curr == 0:
                return (top-base)/2+base
            elif curr == -1:
                top = (top-base)/2 +base
            else:
                base = (top-base)/2 +base
        return base 