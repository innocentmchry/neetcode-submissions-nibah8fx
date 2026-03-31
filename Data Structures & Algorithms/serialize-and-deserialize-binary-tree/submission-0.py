# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Good question to learn .join() and .split() functions
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root):
            if not root:
                res.append('N')
                return
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.idx = 0
        res = data.split(",")

        def dfs():
            if res[self.idx] == 'N':
                self.idx += 1
                return None

            cur_node = TreeNode(int(res[self.idx]))
            self.idx += 1
            cur_node.left = dfs()
            cur_node.right = dfs()

            return cur_node
        
        return dfs()
