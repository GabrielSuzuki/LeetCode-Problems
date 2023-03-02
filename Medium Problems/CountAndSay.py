class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count = "1"
        nextCount = ""
        while n > 1:
            nextCount = ""
            current = count[0]
            currCount = 0
            for i in range(0,len(count)):
                if current == count[i]:
                    currCount += 1
                if current != count[i]:
                    nextCount += str(currCount) + str(current)
                    currCount = 1
                    current = count[i]
                if len(count)-1 == i:
                    nextCount += str(currCount) + str(current)
            n -= 1
            if nextCount != "":
                count = nextCount
        return count