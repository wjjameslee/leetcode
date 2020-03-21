# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            result = ListNode(-1)
            # We use a different variable to track linked list position
            cont_result = result;
            while l1 and l2:
                if l1.val <= l2.val:
                    cont_result.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    cont_result.next = ListNode(l2.val)
                    l2 = l2.next
                cont_result = cont_result.next
            
            while l1:
                cont_result.next = ListNode(l1.val)
                l1 = l1.next
                cont_result = cont_result.next
                
            while l2:
                cont_result.next = ListNode(l2.val)
                l2 = l2.next
                cont_result = cont_result.next
            
            return result.next
