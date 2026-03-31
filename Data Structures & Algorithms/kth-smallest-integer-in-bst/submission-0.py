# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Let me try a brute force way

        res = []

        def dfs(r):
            if not r:
                return            
            res.append(r.val)
            if r.left:
                dfs(r.left)
            if r.right:
                dfs(r.right)

        dfs(root)
        res.sort()

        return res[k-1]