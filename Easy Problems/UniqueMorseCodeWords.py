class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphaDict = {
            'a': ".-",
            'b': "-...",
            'c': "-.-.",
            'd': "-..",
            'e': ".",
            'f': "..-.",
            'g': "--.",
            'h': "....",
            'i': "..",
            'j': ".---",
            'k': "-.-",
            'l': ".-..",
            'm': "--",
            'n': "-.",
            'o': "---",
            'p': ".--.",
            'q': "--.-",
            'r': ".-.",
            's': "...",
            't': "-",
            'u': "..-",
            'v': "...-",
            'w': ".--",
            'x': "-..-",
            'y': "-.--",
            'z':"--.."
        }
        outputDict ={}
        output = 0
        for i in words:
            currWord = ""
            for letter in range(0,len(i)):
                currWord += alphaDict[i[letter]]
            if outputDict.get(currWord) == None:
                output += 1
                outputDict[currWord] = 1
        return output