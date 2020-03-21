# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_exponent = 0
        l2_exponent = 0
        l1_total = 0
        l2_total = 0
        while l1:
            l1_total += l1.val * (10 ** l1_exponent)
            l1_exponent += 1
            l1 = l1.next
        while l2:
            l2_total += l2.val * (10 ** l2_exponent)
            l2_exponent += 1
            l2 = l2.next
        
        finalSum = l1_total + l2_total
        finalDigits = []
        if finalSum == 0:
            return ListNode(0)
        while finalSum:
            finalDigits.append(finalSum % 10)
            finalSum = finalSum // 10
        
        finalList = ListNode(-1)
        head = finalList
        for digit in finalDigits:
            finalList.next = ListNode(digit)
            finalList = finalList.next
        return head.next
            
            
            