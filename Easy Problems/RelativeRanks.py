class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        output = []
        sortedScore = sorted(score,reverse=True)
        tempDict = {}
        for i in range(0,len(sortedScore)):
            tempDict[sortedScore[i]] = i + 1
        for i in range(0,len(score)):
            if tempDict[score[i]] == 1:
                output.append("Gold Medal")
            elif tempDict[score[i]] == 2:
                output.append("Silver Medal")
            elif tempDict[score[i]] == 3:
                output.append("Bronze Medal")
            else:
                output.append(str(tempDict[score[i]]))
        return output