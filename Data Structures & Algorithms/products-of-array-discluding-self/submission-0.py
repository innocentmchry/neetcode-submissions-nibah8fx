class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Let me use division operation first
        total = 1
        number_of_zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                number_of_zeros += 1
                zero_idx = i
            total *= nums[i]


        res = [0] * len(nums)
        if number_of_zeros > 1:
            return res
        elif number_of_zeros == 1:
            temp = 1
            for i in range(len(nums)):
                if i == zero_idx:
                    continue
                temp *= nums[i]
            res[zero_idx] = temp
        else:
            for i in range(len(nums)):
                res[i] = int(total / nums[i])

        return res