# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        lh = self.maxHeight(root.left)
        rh = self.maxHeight(root.right)
        diamater = lh + rh
        sub_left = self.diameterOfBinaryTree(root.left)
        sub_right = self.diameterOfBinaryTree(root.right)
        return max(diamater,sub_left,sub_right)



    def maxHeight(self,root):
        if root is None:
            return 0
        return 1 + max(self.maxHeight(root.left),self.maxHeight(root.right))