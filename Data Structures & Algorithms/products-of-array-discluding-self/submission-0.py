class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        n = len(nums)
        out = [1] * n
        for i in range(n):
            out[i] *= left
            out[n-1-i] *= right
            left *= nums[i]
            right *= nums[n-1-i]
        return out
            