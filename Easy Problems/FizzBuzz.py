class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        strArr = []

        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                strArr.append("FizzBuzz")
            elif i % 3 == 0:
                strArr.append("Fizz")
            elif i % 5 == 0:
                strArr.append("Buzz")
            else:
                strArr.append(str(i))
        return strArr