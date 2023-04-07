class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        newString = sentence.split(" ")
        vowels = ["a","e","i","o","u"]
        output = ""
        for i in range(0,len(newString)):
            if newString[i][0].lower() in vowels:
                newString[i] += "ma" + ("a" * (i+1))
            else:
                newString[i] = newString[i][1:] + newString[i][0] + "ma" + ("a" * (i+1))
        for i in range(0,len(newString)):
            output += newString[i]
            if i != len(newString) - 1:
                output += " "
        return output