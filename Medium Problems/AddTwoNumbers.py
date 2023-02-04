# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tempWord1 = ""
        tempWord2 = ""
        #newNode = ListNode()
        pastNode = ListNode()
        while l1 != None:
            tempWord1 += str(l1.val)
            l1 = l1.next
        while l2 != None:
            tempWord2 += str(l2.val)
            l2 = l2.next
        tempWord1 = tempWord1[::-1]
        tempWord2 = tempWord2[::-1]
        newNum = str(int(tempWord1) +int(tempWord2))
        newNode = ListNode(int(newNum[0]),None)
        pastNode = newNode
        for i in range(1,len(newNum)):
            newNode = ListNode(int(newNum[i]),pastNode)
            pastNode = newNode 
        return(newNode)
