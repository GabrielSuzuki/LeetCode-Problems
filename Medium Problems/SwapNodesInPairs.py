# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        count = 1
        if head == None:
            return None
        if head.next == None:
            return head
        while temp != None:
            if count % 2 == 1:
                if temp.next == None:
                    return head
                tempVal = temp.next.val
                temp.next.val = temp.val
                temp.val = tempVal
            count += 1
            temp = temp.next
        return head