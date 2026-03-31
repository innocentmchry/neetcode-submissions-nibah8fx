# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Concept of preorder, inorder, postorder traversal
        
        res = []
        def dfs(r):
            # if not r:
            #     return
            
            if r.left:
                dfs(r.left)
            
            res.append(r.val)

            if r.right:
                dfs(r.right)

        dfs(root)
        return res[k-1]
        