class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = sorted(stones,reverse=True)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                stones[0] = stones[0] - stones[1]
                stones.pop(1)
                stones = sorted(stones,reverse=True)
        if len(stones) == 0:
            return 0
        return stones[0]