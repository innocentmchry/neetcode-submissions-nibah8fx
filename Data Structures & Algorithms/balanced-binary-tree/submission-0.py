# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.status = True
        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            diff = left - right
            if diff < -1 or diff > 1:
                self.status = False 

            longest = max(left, right)

            return 1 + longest

        dfs(root)
        return self.status