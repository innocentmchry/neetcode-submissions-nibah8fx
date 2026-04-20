class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        stack.append((temperatures[0], 0))
        for i in range(1, len(temperatures)):
            curval, curidx = temperatures[i], i
            
            while stack and curval > stack[-1][0]:
                entryidx = stack.pop()[1]
                res[entryidx] = curidx - entryidx

            stack.append((curval, curidx))

        return res
