# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Recursive solution

        def search(ls, mid):
            for i in range(len(ls)):
                if mid == ls[i]:
                    return i

        def build(preorder, inorder):
            if not preorder or not inorder:
                return

            root = TreeNode(preorder[0])
            mid = search(inorder, preorder[0])
            root.left = build(preorder[1: 1 + mid], inorder[0: mid])
            root.right = build(preorder[1 + mid:], inorder[mid + 1:])
            
            return root

        return build(preorder, inorder)
