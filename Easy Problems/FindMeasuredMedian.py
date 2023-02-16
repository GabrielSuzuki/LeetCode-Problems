class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newSortedArr = sorted(nums1+nums2)
        n = len(newSortedArr)
        print(newSortedArr[(n/2)-1],newSortedArr[n/2])
        if n % 2 == 0:
            return (newSortedArr[(n/2)-1] + newSortedArr[n/2])/2.0
        else:
            return (newSortedArr[n/2])