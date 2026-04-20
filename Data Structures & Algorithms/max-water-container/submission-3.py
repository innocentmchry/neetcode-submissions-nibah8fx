class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxarea = 0

        while l < r:
            h = min(heights[l], heights[r])
            dist = r - l
            area = h * dist
            maxarea = max(maxarea, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxarea
