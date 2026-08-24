"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_dummy = Node(0,head)
        pointer_old = head
        dummy = Node(0)
        pointer_new = dummy
        old_to_new = {None:None}
        while pointer_old:
            new_node = Node(pointer_old.val)
            pointer_new.next = new_node
            old_to_new[pointer_old] = new_node
            pointer_old = pointer_old.next
            pointer_new = pointer_new.next
        pointer_old = head
        pointer_new = dummy.next
        while pointer_old:
            new_random = old_to_new.get(pointer_old.random)
            pointer_new.random = new_random
            pointer_old = pointer_old.next
            pointer_new = pointer_new.next
        return dummy.next


        