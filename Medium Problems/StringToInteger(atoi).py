class Solution(object):
    def clamp(self,n, smallest, largest):
        return max(smallest, min(n, largest))
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        final = ""
        start = True
        if s == "":
            return 0
        #if not s.isdigit():
        #    return 0
        hasDigit = False
        for j in s:
            if j.isdigit():
                hasDigit = True
                break
        if hasDigit == False:
            return 0
        for i in range(0,len(s)):
            if s[i] == " ":
                if start == False:
                    if final != "" and final != "-" and final != "+":
                        return self.clamp(int(final),-2**31,2**31-1)
                    else:
                        return 0
                continue
            elif s[i] == '-':
                if start == False:
                    if final != "" and final != "-" and final != "+":
                        return self.clamp(int(final),-2**31,2**31-1)
                    return 0
                final += '-'
                start = False
            elif s[i] == '+':
                if start == False:
                    if final != "" and final != "-" and final != "+":
                        return self.clamp(int(final),-2**31,2**31-1)
                    return 0
                #final += '+'
                start = False
            elif s[i].isdigit():
                final += s[i]
                start = False
            else:
                if start == False:
                    if final != "" and final != "-" and final != "+":
                        return self.clamp(int(final),-2**31,2**31-1)
                    else:
                        return 0
                else:
                    return 0
        return self.clamp(int(final),-2**31,2**31-1)
