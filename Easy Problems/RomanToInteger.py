class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if len(s) != i+1:
                    if s[i+1] == 'I':
                        total += 1
                    elif s[i+1] == 'V':
                        i += 2
                        total += 4
                    elif s[i+1] == 'X':
                        i += 2
                        total += 9
                    else:
                        total += 1
                else:
                    total += 1
            elif s[i] == 'X':
                if len(s) != i+1:
                    if s[i+1] == 'X':
                        total += 10
                    elif s[i+1] == 'L':
                        i += 1
                        total += 40
                    elif s[i+1] == 'C':
                        i += 1
                        total += 90
                    else:
                        total += 10
                else:
                    total += 10
            elif s[i] == 'C':
                #print("enter",i)
                if len(s) != i+1:
                    if s[i+1] == 'C':
                        total += 100
                    elif s[i+1] == 'D':
                        i += 1
                        total += 400
                    elif s[i+1] == 'M':
                        i += 1
                        total += 900
                    else:
                        total += 100
                else:
                    total += 100

            elif s[i] == 'V':
                total += 5
            elif s[i] == 'L':
                total += 50
            elif s[i] == 'D':
                total += 500
            else:
                total += 1000
            #print(total,i)
            i += 1
        return total