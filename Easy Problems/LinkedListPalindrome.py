# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        n = 0
        stack = []
        if head.next == None:
            return True
        while temp != None:
            n += 1
            temp = temp.next
        temp = head
        currCount = 1
        if n%2 == 0:
            while temp != None:
                if n/2 >= currCount:
                    stack.append(temp.val)
                else:
                    if stack.pop() != temp.val:
                        return False
                currCount += 1
                temp = temp.next
        else:
            while temp != None:
                if currCount < n/2+1:
                    stack.append(temp.val)
                elif currCount > n/2+1:
                    if stack.pop() != temp.val:
                        return False
                currCount += 1
                temp = temp.next
        return True