class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > target or nums[-1] < target:
            return -1
        n = len(nums)
        index = n // 2
        i = 4
        while True:
            step = math.ceil(n/i)
            i *=2
            if step == 0:
                return -1
            current = nums[index]
            if current == target:
                return index
            elif current < target:
                index += step
            else:
                index -= step
            

