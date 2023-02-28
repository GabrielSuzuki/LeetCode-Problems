class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        k = len(nums)
        frontFound = False
        endFound = False
        outputArr = [0,0]
        if nums == []:
            return [-1,-1]
        while i <= k:
            #print(i,k,target,nums[i],nums[k-1])
            if nums[i] == target and frontFound == False:
                outputArr[0] = i
                frontFound = True
            elif frontFound == False:
                i += 1
            if nums[k-1] == target and endFound == False:
                outputArr[1] = k-1
                endFound = True
            elif endFound == False:
                k -= 1
            if endFound and frontFound:
                return outputArr
        if not endFound and not frontFound:
            return [-1,-1]
        return outputArr