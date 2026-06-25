class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        beforeMap = {}
        for i, n in enumerate(nums):
            delta = target - n
            if delta in beforeMap:
                return [beforeMap[delta], i]
            beforeMap[n] = i
