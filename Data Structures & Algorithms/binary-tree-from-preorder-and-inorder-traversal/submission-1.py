# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Revision Solution

        def search(element, inorder):
            for i, num in enumerate(inorder):
                if num == element:
                    return i

        # 1 2 4 5 3 6 7
        # 4 2 5 1 6 3 7
        # 0 1 2 3 4 5 6 :idx

        def build(preorder, inorder):
            if not preorder or not inorder:
                return
            
            root = TreeNode(preorder[0])
            mid = search(preorder[0], inorder) #mid = 3
            root.left = build(preorder[1 : mid + 1], inorder[: mid])
            root.right = build(preorder[mid + 1:], inorder[mid + 1:])
            
            return root

        return build(preorder, inorder)


