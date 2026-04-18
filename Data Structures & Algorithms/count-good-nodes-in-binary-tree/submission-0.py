# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if root is None:
            return 0

        self.good = 0

        def dfs(cur_max, root):
            if root is None:
                return
    
            if root.val >= cur_max:
                self.good += 1
                cur_max = root.val

            dfs(cur_max, root.left)
            dfs(cur_max, root.right)
            return
        
        dfs(root.val, root)

        return self.good