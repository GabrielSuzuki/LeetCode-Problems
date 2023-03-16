class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        newList = s.split(" ")
        newString = ""
        for i in newList:
            for j in range(len(i)-1,-1,-1):
                newString += i[j]
            newString += " "
        newString = newString[:-1]
        return newString