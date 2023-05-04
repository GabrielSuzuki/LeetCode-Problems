class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        output = ""
        for i in range(0,len(address)):
            if address[i] != ".":
                output += address[i]
            else:
                output += "[.]"
        return output