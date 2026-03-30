# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(r):
            if r is None:
                return
            elif r.left is not None and r.right is not None:
                r.left, r.right = r.right, r.left
                invert(r.left)
                invert(r.right)
            elif r.left is not None:
                r.right = r.left
                r.left = None
                invert(r.right)
            else:
                r.left = r.right
                r.right = None
                invert(r.left)
        
        invert(root)
        return root
                
        