# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        count = 1
        length = 0
        while temp != None:
            length += 1
            temp = temp.next
        temp = head
        if length == 1 and n == 1:
            return None
        if (length - n) < count:
            return head.next
        else:
            while count < length - n:
                head = head.next
                count += 1
            head.next = head.next.next
        return temp