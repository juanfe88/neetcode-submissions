# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k ==1:
            return head
        dummy = ListNode(0,head)
        prev = dummy
        while prev:
            scout = prev
            for _ in range(k):
                if scout is None:
                    break
                scout = scout.next
            if scout is None:
                break
            anchor = prev.next
            to_move = anchor.next
            for _ in range(k-1):
                anchor.next = to_move.next
                to_move.next = prev.next
                prev.next = to_move
                to_move = anchor.next
            prev = anchor
        return dummy.next