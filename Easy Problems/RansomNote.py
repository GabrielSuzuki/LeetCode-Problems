class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomDict = {}
        magDict = {}
        if len(ransomNote) > len(magazine):
            return False
        if ransomNote == magazine:
            return True
        for i in range(0,len(ransomNote)):
            if ransomDict.get(ransomNote[i]) == None:
                ransomDict[ransomNote[i]] = 1
            else:
                ransomDict[ransomNote[i]] += 1
        for i in range(0,len(magazine)):
            if magDict.get(magazine[i]) == None:
                magDict[magazine[i]] = 1
            else:
                magDict[magazine[i]] += 1
        for i in list(ransomDict.keys()):
            if magDict.get(i) == None:
                return False
            if ransomDict[i] > magDict[i]:
                return False
        return True