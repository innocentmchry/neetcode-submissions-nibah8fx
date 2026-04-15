"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Its just a dfs solution why I forgot I have no Idea
        hashmap = {}
        if node is None:
            return None

        def dfs(node):
            if node.val in hashmap:
                return hashmap[node.val]

            copy = Node(node.val)
            hashmap[node.val] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)