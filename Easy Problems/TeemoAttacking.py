class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = duration
        for i in range(1,len(timeSeries)):
            if duration > timeSeries[i] - timeSeries[i-1]:
                total += timeSeries[i] - timeSeries[i-1]
            else:
                total += duration     
        return total