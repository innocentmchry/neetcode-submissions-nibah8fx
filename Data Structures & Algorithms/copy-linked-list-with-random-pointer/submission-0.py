"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # I think this is going to be dfs as well
        if head is None:
            return None

        hashmap = {}

        def dfs(head):
            if head in hashmap:
                return hashmap[head]

            # I actually dont need the val-new hashmap, i can use old-new hashmap
            copy = Node(head.val)
            hashmap[head] = copy

            # process next
            if head.next:
                copy.next = dfs(head.next)

            # process random   
            if head.random:
                copy.random = dfs(head.random)

            return copy

        return dfs(head)