# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkequality(p, q):
            if p is None and q is None:
                return True
            
            if p is None or q is None or p.val != q.val:
                return False
            
            return checkequality(p.left, q.left) and checkequality(p.right, q.right)

        stack = []
        stack.append(root)
        if len(stack) == 0:
            return False

        while stack:
            cur = stack.pop()
            if cur.val == subRoot.val:
                status = checkequality(cur, subRoot)
                if status:
                    return True

            if cur.right: 
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return False