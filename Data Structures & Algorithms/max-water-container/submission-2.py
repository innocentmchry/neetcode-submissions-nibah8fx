class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0
        # [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
        while left <= right:
            area = (right - left) * min(heights[left], heights[right])
            if area > res:
                res = area
                  
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1

        return res