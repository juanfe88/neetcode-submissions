# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
            if fast == slow:
                return True

        return False
        