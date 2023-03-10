class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nextNum = False
        output = []
        for i in nums1:
            nextNum = False
            for j in range(0,len(nums2)):
                if nums2[j] == i:
                    nextNum = True
                elif nextNum and nums2[j] > i:
                    output.append(nums2[j])
                    break
                if j == len(nums2) - 1:
                    output.append(-1)
        return output