class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        currRow = ""
        output = []
        for i in range(0,len(words)):
            n = len(words[i])
            for j in range(0,n):
                if j == 0:
                    if words[i][j].lower() in row1:
                        currRow = row1
                    elif words[i][j].lower() in row2:
                        currRow = row2
                    else:
                        currRow = row3
                elif words[i][j].lower() not in currRow:
                    break
                if j == n-1:
                    output.append(words[i])
        return output