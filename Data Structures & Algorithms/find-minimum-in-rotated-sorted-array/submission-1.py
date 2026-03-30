class Solution:
    def findMin(self, nums: List[int]) -> int:
        minm = 1001
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < minm:
                minm = nums[mid]

            if nums[left] < nums[right]:
                if nums[left] < nums[mid]:
                    cur_min_idx = left
                else:
                    cur_min_idx = mid
            else:
                if nums[right] < nums[mid]:
                    cur_min_idx = right
                else:
                    cur_min_idx = mid
            
            if left == cur_min_idx or mid == cur_min_idx:
                right = mid - 1
            else:
                left = mid + 1
        return minm