class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n) Solution
        res = [0] * len(temperatures)
        stack = [] # pair of idx, values

        for i, value in enumerate(temperatures):
            while stack and stack[-1][1] < value:
                idx, curvalue = stack.pop()
                res[idx] = i - idx
            stack.append([i, value])

        return res