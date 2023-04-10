# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        n = 0
        while temp != None:
            temp = temp.next
            n += 1
        for i in range(0,n//2):
            head = head.next
        return head