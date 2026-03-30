# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Do I want to try an interative solution:
        # Sometimes recursive solutions are just easier

        # Must use DFS and for DFS you need a stack
        stack = []
        if not p and not q:
            return True
        else:
            stack.append((p, q))

        while stack:            
            p1, p2 = stack.pop()

            if (p1 == None and p2 != None) or (p1 != None and p2 == None):
                return False

            if p1 == None and p2 == None:
                continue

            if p1.val != p2.val:
                return False

            stack.append((p1.right, p2.right))            
            stack.append((p1.left, p2.left))

        return True


