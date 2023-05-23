# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        binStr = "0b"
        while head != None:
            binStr += str(head.val)
            head = head.next 
        return int(binStr,0)