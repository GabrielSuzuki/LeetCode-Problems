class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        billDict = {
            "5" : 0,
            "10" : 0
        }
        for i in bills:
            if i == 5:
                billDict["5"] += 1
            elif i == 10:
                if billDict["5"] == 0:
                    return False
                else:
                    billDict["5"] -= 1
                    billDict["10"] += 1
            else:
                if billDict["5"] > 0 and billDict["10"] > 0:
                    billDict["5"] -= 1
                    billDict["10"] -= 1
                elif billDict["5"] >= 3:
                    billDict["5"] -= 3
                else:
                    return False
        return True