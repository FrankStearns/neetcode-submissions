class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        out = 0
        for num in nums:
            if num - 1 in nums:
                continue
            i = 1
            while num + i in nums:
                i += 1
            if out < i:
                out = i
        return out