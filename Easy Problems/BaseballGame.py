class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        for i in operations:
            if i == "+":
                record.append(record[-1]+record[-2])
            elif i == "D":
                record.append(record[-1]*2)
            elif i == "C":
                record.pop()
            else:
                record.append(int(i))
        return sum(record)