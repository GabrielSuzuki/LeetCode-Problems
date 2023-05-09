class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        output = []
        for i in arr2:
            for j in arr1:
                if j == i:
                    output.append(j)
        for j in sorted(arr1):
            if j not in arr2:
                output.append(j)
        return output