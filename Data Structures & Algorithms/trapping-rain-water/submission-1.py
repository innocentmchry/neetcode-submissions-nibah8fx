class Solution:
    def trap(self, height: List[int]) -> int:
        # You can solve this question using two pointers as well in O(1) space

        maxleft, maxright = height[0], height[len(height) - 1]
        l, r = 0, len(height) - 1

        total = 0
        while l < r:
            if maxleft <= maxright:
                l += 1
                maxleft = max(maxleft, height[l])
                val = min(maxleft, maxright) - height[l]

            else:
                r -= 1
                maxright = max(maxright, height[r])
                val = min(maxleft, maxright) - height[r]
            
            if val > 0:
                total += val

        return total
