class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper():
            return True
        if word.islower():
            return True
        if word[0].isupper():
            for i in range(1,len(word)):
                if word[i].isupper():
                    return False
            return True
        return False