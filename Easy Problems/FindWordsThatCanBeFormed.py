class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        charDict = {}
        output = 0
        for i in range(0,len(chars)):
            if chars[i] not in charDict:
                charDict[chars[i]] = 1
            else:
                charDict[chars[i]] += 1
        for i in words:
            tempDict = {}
            for j in range(0,len(i)):
                if i[j] not in charDict:
                    break
                if i[j] not in tempDict:
                    tempDict[i[j]] = 1
                else:
                    tempDict[i[j]] += 1
                    if tempDict[i[j]] > charDict[i[j]]:
                        break
                if j == len(i) - 1:
                    output += len(i)
        return output