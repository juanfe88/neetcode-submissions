# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2
        merge_dumy = ListNode(0)
        main_pointer = merge_dumy
        while pointer1 or pointer2:
            if pointer2 is None:
                main_pointer.next = pointer1
                pointer1 = pointer1.next
                main_pointer = main_pointer.next
                main_pointer.next = None
            elif pointer1 is None:
                main_pointer.next = pointer2
                pointer2 = pointer2.next
                main_pointer = main_pointer.next
                main_pointer.next = None
            else:
                if pointer1.val<pointer2.val:
                    main_pointer.next = pointer1
                    pointer1 = pointer1.next
                    main_pointer = main_pointer.next
                    main_pointer.next = None
                else:
                    main_pointer.next = pointer2
                    pointer2 = pointer2.next
                    main_pointer = main_pointer.next
                    main_pointer.next = None
        return merge_dumy.next