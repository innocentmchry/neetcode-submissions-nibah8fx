class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def addword(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        
        root = TrieNode()
        for word in words:
            root.addword(word)

        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r not in range(rows) or c not in range(cols) or
                board[r][c] not in node.children or
                (r,c) in visit):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            
            visit.remove((r,c))


        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")

        return list(res)