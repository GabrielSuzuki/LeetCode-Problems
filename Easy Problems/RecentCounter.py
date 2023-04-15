class RecentCounter(object):

    def __init__(self):
        self.counter = 0
        self.counterList = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.counterList.append(t)
        i = 0
        while self.counterList[i] < t - 3000:
            self.counterList.pop(0)
        self.counter = len(self.counterList)
        return self.counter
