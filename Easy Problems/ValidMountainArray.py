class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False
        decreasing = False
        for i in range(2,len(arr)):
            if arr[i] == arr[i-1]:
                return False
            if decreasing:
                if arr[i-1] < arr[i]:
                    return False
            else:
                if arr[i-1] > arr[i]:
                    decreasing = True
        if decreasing:
            return True
        return False