# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        tempNode = ListNode()
        stack = []
        while temp != None:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while stack != []:
            head.val = stack.pop()
            head = head.next
        return temp