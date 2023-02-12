class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        tempNum = str(num)[::-1]
        outputStr = ""
        for i in range(len(tempNum)-1,-1,-1):
            print(tempNum[i],i)
            if i == 3:
                outputStr += "M" * int(tempNum[i])
            if i == 2:
                if tempNum[i] == "5":
                    outputStr += "D"
                elif tempNum[i] == "9":
                    outputStr += "CM"
                elif tempNum[i] == "4":
                    outputStr += "CD"
                else:
                    if tempNum[i] > "5":
                        outputStr += "D" + "C" * (int(tempNum[i])-5)
                    else:
                        outputStr += "C" * int(tempNum[i])
            if i == 1:
                if tempNum[i] == "5":
                    outputStr += "L"
                elif tempNum[i] == "9":
                    outputStr += "XC"
                elif tempNum[i] == "4":
                    outputStr += "XL"
                else:
                    if tempNum[i] > "5":
                        outputStr += "L" + "X" * (int(tempNum[i])-5)
                    else:
                        outputStr += "X" * int(tempNum[i])
            if i == 0:
                if tempNum[i] == "5":
                    outputStr += "V"
                elif tempNum[i] == "9":
                    outputStr += "IX"
                elif tempNum[i] == "4":
                    outputStr += "IV"
                else:
                    if tempNum[i] > "5":
                        outputStr += "V" + "I" * (int(tempNum[i])-5)
                    else:
                        outputStr += "I" * int(tempNum[i])
        return outputStr