# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def checkequality(p, q) -> bool:
            if p == None and q == None:
                return True
            if (p == None and q != None) or (p != None and q == None) or p.val != q.val:
                return False
            else:
                return checkequality(p.left, q.left) and checkequality(p.right, q.right)
        
        return checkequality(p, q)