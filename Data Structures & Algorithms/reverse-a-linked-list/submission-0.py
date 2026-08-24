# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev = head
        pointer = prev.next
        while pointer:
            prev.next = pointer.next
            pointer.next = dummy.next
            dummy.next = pointer
            pointer = prev.next
        return dummy.next


