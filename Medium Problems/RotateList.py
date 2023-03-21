class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp = head
        tempArr = []
        if head == None:
            return head
        while head != None:
            tempArr.append(head.val)
            head = head.next
        if k > len(tempArr):
            k %= len(tempArr)
        tempArr = tempArr[-k:]+tempArr[:-k]
        temp2 = temp
        i = 0
        while temp != None:
            temp.val = tempArr[i]
            i += 1
            temp = temp.next
        return temp2