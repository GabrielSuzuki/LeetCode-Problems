class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0,0
        for i in range(0,len(moves)):
            if moves[i] == 'U':
                y += 1
            elif moves[i] == 'D':
                y -= 1
            elif moves[i] == 'L':
                x -= 1
            elif moves[i] == 'R':
                x += 1
        if x == y == 0:
            return True
        else:
            return False