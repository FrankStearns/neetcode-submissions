class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        n = len(nums)
        out = [1] * n
        for i in range(n):
            end = n - i - 1
            out[i] *= left
            out[end] *= right
            left *= nums[i]
            right *= nums[end]
        return out
            