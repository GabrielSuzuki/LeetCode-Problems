class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = head
        while head != None:
            if head.next != None:
                if head.next.val == head.val:
                    head.next = head.next.next
                else:
                    head = head.next
            else:
                break
        return prev