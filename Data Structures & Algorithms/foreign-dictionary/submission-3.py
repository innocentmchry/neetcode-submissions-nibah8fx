class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for ch in word:
                graph[ch] = set()

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            minlen = min(len(word1), len(word2))
            if word1[:minlen] == word2[:minlen] and len(word1) > len(word2):
                return ""
            for j in range(minlen):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break

        visited = set()
        cycle = set()
        res = []
        def dfs(ch):            
            if ch in cycle:
                return True
            
            if ch in visited:
                return False

            visited.add(ch)
            cycle.add(ch)
            for nei in graph[ch]:
                if dfs(nei):
                    return ""
                
            res.append(ch)
            cycle.remove(ch)

        for ch in graph:
            if dfs(ch):
                return ""

        res.reverse()
        return "".join(res)