# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST I know
        # gotta find a recursive solution

        def my_func(root: TreeNode, l, r) -> bool:
            if root is None:
                return True
            
            if not (l < root.val < r):
                return False
            
            return my_func(root.left, l, root.val) and my_func(root.right, root.val, r)

        return my_func(root, -float('infinity'), float('infinity'))
