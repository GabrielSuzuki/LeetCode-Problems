class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        output = []
        for email in emails:
            splitEmails = email.split("@")
            newFirst = ""
            newSec = ""
            for i in range(0,len(splitEmails[0])):
                if splitEmails[0][i] == "+":
                    break
                if splitEmails[0][i].isalpha():
                    newFirst += splitEmails[0][i]
            for j in range(0,len(splitEmails[1])):
                newSec += splitEmails[1][j]
            if (newFirst + "@" + newSec) not in output:
                output.append((newFirst + "@" + newSec))
        return len(output)