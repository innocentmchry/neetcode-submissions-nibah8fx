# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        res = []
        
        def bfs(root, level):
            if root is None:
                return None
            
            if level == len(res):
                res.append(root.val)

            bfs(root.right, level+1)
            bfs(root.left, level+1)

        bfs(root, 0)
        return res
            
        


