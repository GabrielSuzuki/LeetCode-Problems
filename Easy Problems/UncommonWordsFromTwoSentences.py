class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1Dict = {}
        s2Dict = {}
        s1List = s1.split(" ")
        s2List = s2.split(" ")
        output = []
        for i in s1List:
            if i not in s1Dict:
                s1Dict[i] = 1
            else:
                s1Dict[i] += 1
        for j in s2List:
            if j not in s2Dict:
                s2Dict[j] = 1
            else:
                s2Dict[j] += 1
        for i in list(s1Dict.keys()):
            if s1Dict[i] == 1 and i not in s2Dict:
                output.append(i)
        for j in list(s2Dict.keys()):
            if s2Dict[j] == 1 and j not in s1Dict:
                output.append(j)
        return output