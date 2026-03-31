# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        
        def dfs(r):
            if not r:
                return
            
            dfs(r.left)            
            self.k -= 1
            if self.k == 0:
                self.result = r.val
            
            dfs(r.right)

        dfs(root)
        return self.result