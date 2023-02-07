class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        increment = 1
        total = 0
        output = []
        for i in range(len(digits)-1,-1,-1):
            total += digits[i] * increment
            increment *= 10
        total += 1
        for i in range(0,len(str(total))):
            output.append(int(str(total)[i]))
        return output