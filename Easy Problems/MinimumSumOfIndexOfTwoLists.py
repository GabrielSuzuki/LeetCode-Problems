class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        intDict = {}
        output = []
        for i in range(0,len(list1)):
            if intDict.get(list1[i]) == None and list1[i] in list2:
                intDict[list1[i]] = i
        for j in range(0,len(list2)):
            if intDict.get(list2[j]) != None:
                intDict[list2[j]] += j
        minimum = min(list(intDict.values()))
        for i in list(intDict.keys()):
            if intDict[i] == minimum:
                output.append(i)
        return output