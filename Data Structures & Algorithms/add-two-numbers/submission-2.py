# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer_1 = l1
        pointer_2 = l2
        dummy = ListNode(0)
        pointer_sum = dummy
        carry = 0
        while pointer_1 or pointer_2:
            new_node = ListNode(0)
            val = 0
            if pointer_1 :
                val += pointer_1.val
                pointer_1 = pointer_1.next
            if pointer_2 :
                val += pointer_2.val
                pointer_2 = pointer_2.next
            if carry > 0:
                val += carry
            if val > 9:
                carry = 1
                val -= 10
            else:
                carry = 0
            new_node.val = val
            pointer_sum.next = new_node
            pointer_sum = pointer_sum.next
        if carry>0:
            new_node = ListNode(carry)
            pointer_sum.next = new_node

        return dummy.next