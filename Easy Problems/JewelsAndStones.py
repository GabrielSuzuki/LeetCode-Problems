class Solution(object):
    def numJewelsInStones(self, jewel, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewelDict = {}
        output = 0
        for i in range(0,len(jewel)):
            if jewelDict.get(jewel[i]) == None:
                jewelDict[jewel[i]] = 1
            else:
                jewelDict[jewel[i]] += 1
        for i in range(0,len(stones)):
            if stones[i] in jewelDict:
                output += 1
        return output