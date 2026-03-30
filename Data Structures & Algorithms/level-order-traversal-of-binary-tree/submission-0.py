# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        fl = []
        if root is None:
            return []
    
        def bfs(root):
            while(q):           
                templs = []
                level = len(q)
                for i in range(level):
                    curr = q.popleft()
                    if curr.left is not None:
                        q.append(curr.left)
                    if curr.right is not None:
                        q.append(curr.right)

                    templs.append(curr.val)

                fl.append(templs)

        bfs(root)
        return fl
                