# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        reverse_val = []
        
        reverseHead = ListNode(-1)
        reverseList = reverseHead

        while head:
            reverse_val.append(head.val)
            head = head.next
            
        l = len(reverse_val)
        for i in range(l-1, -1, -1):
            reverseList.next = ListNode(reverse_val[i])
            reverseList = reverseList.next
        return reverseHead.next
        '''
        cur = head
        prev = None
        
        while cur:
            next = cur.next # Need temp variable to change from current node to next node
            cur.next = prev
            prev = cur
            cur = next
        return prev
            
        