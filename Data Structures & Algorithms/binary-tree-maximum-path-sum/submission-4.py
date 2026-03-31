# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def my_func(root):
            if not root:
                return 0

            left_max = max(0, my_func(root.left))
            right_max = max(0, my_func(root.right))
            
            cur_max = root.val + left_max + right_max

            self.res = max(self.res, cur_max)

            return root.val + max(left_max, right_max)

        my_func(root)
        return self.res