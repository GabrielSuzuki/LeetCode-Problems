class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        count = 1
        temp = head
        tempStack = []
        while count <= right:
            if count >= left and count <= right:
                tempStack.append(temp.val)
            temp = temp.next
            count += 1
        temp = head
        count = 1
        while count <= right:
            if count >= left and count <= right:
                temp.val = tempStack.pop()
            temp = temp.next
            count += 1
        return head