class Solution:
    def trap(self, height: List[int]) -> int:
        # A little inefficient solution would be
        # create check min max both left and right
        # Better to store in an array both min max values
        size = len(height)
        maxleft = [0] * size
        maxright = [0] * size

        #minleft 
        curmax = height[0]
        for i in range(1, size):
            curmax = max(height[i-1], curmax)
            maxleft[i] = curmax

        curmax = height[size-1]
        for i in range(size-2, -1, -1):
            curmax = max(height[i+1], curmax)
            maxright[i] = curmax

        total = 0
        for i in range(size):
            val = min(maxleft[i], maxright[i]) - height[i]
            if val > 0:
                total += val

        return total