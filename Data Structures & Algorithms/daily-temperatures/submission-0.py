class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = [0] * size
        # 2, 1, 5
        # 0, 1, 2
        for i in range(size):
            for j in range(i+1, size):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break

        return res

