# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cp = l2
        while True:
            v1 = l1.val
            v2 = l2.val
            s = v1 + v2 + carry
            q, r = divmod(s, 10)
            l2.val = r
            carry = q

            l1_prev = l1
            l2_prev = l2
    
            l1 = l1_prev.next
            l2 = l2_prev.next

            if not l1 and not l2:
                if carry:
                    l2_prev.next = ListNode(carry)
                break

            if not l1 and l2:
                l1_prev.next = l1 = ListNode()

            if not l2 and l1:
                l2_prev.next = l2 = ListNode()
        return cp
