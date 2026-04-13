class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Let me try the brute force method
        max_area = 0
        for i in range(len(heights)):
            l, r = i, i
            while l > -1 and heights[l] >= heights[i]:
                l -= 1
            
            while r < len(heights) and heights[r] >= heights[i]:
                r += 1

            cur_area = (r - l - 1) * heights[i]
            max_area = max(cur_area, max_area)

        return max_area