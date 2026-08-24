# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, offset = head, head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for _ in range(n):
            offset = offset.next
        while offset:
            pre = slow
            slow = slow.next
            offset = offset.next
        pre.next = slow.next
        slow.next = None

        return dummy.next