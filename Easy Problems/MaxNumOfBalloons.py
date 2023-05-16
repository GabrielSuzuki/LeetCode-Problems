class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        charDict = {
            'b' : 0,
            'l' : 0,
            'a' : 0,
            'o' : 0,
            'n' : 0
        }
        output = 0
        for i in range(0,len(text)):
            if text[i].lower() in charDict:
                charDict[text[i].lower()] += 1
        while charDict['b'] >= 1 and charDict['l'] >= 2 and charDict['a'] >= 1 and charDict['o'] >= 2 and charDict['n'] >= 1:
            charDict['b'] -= 1
            charDict['l'] -= 2
            charDict['a'] -= 1
            charDict['o'] -= 2
            charDict['n'] -= 1
            output += 1
        return output