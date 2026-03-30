class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        def bs(curr, left, right, arr):
            pos = len(arr) # default position in case no one is larger
            while(left <= right):
                mid = (left + right) // 2
                if curr <= arr[mid]:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            return pos


        ls = []
        if nums:
            ls.append(nums[0])

        for i in range(1, len(nums)):
            flag = False
            c = nums[i]
            left = 0
            right = len(ls) - 1
            pos = bs(c, left, right, ls)

            if pos == len(ls):
                ls.append(c)
            else:
                ls[pos] = c

        return len(ls)