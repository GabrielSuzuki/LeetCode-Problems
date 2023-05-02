class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        output = []
        stringArr = text.split(" ")
        for i in range(0,len(stringArr)-2):
            if stringArr[i] == first and stringArr[i+1] == second:
                output.append(stringArr[i+2])
        return output