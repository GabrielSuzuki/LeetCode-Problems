class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arrSorted = sorted(arr)
        output = []
        mini = arrSorted[1] - arrSorted[0] 
        for i in range(2,len(arrSorted)):
            mini = min(arrSorted[i] -arrSorted[i-1],mini)
        for i in range(1,len(arrSorted)):
            if arrSorted[i] - arrSorted[i-1] == mini:
                output.append([arrSorted[i-1],arrSorted[i]])
        return output