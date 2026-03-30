class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                dist = j - i
                area = dist * min(heights[i], heights[j])
                if area > res:
                    res = area

        return res
        