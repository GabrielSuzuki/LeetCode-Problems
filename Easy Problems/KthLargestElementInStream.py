class KthLargest(object):
    listN = []
    k = 0
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.listN = sorted(nums)
        self.k = k
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.listN.append(val)
        self.listN = sorted(self.listN)
        return self.listN[len(self.listN)-self.k]