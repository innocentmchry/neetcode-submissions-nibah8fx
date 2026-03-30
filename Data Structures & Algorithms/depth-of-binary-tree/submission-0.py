# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(r):
            if r is None:
                return 0
            
            return max(1 + dfs(r.left), 1 + dfs(r.right)) # 1 + because its not none

        return dfs(root)