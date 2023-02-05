class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(0,len(s)):
            #print(stack,s[i])
            if s[i] == '[':
                stack.append('[')
            elif s[i] == '{':
                stack.append('{')
            elif s[i] == '(':
                stack.append('(')
            elif s[i] == ']':
                if stack == []:
                    return False
                if stack.pop() != '[':
                    return False
            elif s[i] == '}':
                if stack == []:
                    return False
                if stack.pop() != '{':
                    return False
            elif s[i] == ')':
                if stack == []:
                    return False
                if stack.pop() != '(':
                    return False   
            #print(stack)
        if stack != []:
            return False
        else:
            return True