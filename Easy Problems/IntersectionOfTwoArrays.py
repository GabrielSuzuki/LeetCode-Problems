class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = list(filter(lambda x: x in nums1, nums2))
        newList = []
        for item in result:
            if item not in newList:
                newList.append(item)
        return newList