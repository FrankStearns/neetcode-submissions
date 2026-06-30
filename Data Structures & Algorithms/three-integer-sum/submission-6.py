class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        out = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            j = i+1
            k = n-1

            while j < k:
                summation = nums[j] + nums[k]
                if summation == target:
                    out.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                if summation < target:
                    j += 1
                if summation > target:
                    k -= 1
        return out 
