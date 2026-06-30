class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            sum = 0
            j = i+1
            while j < n:
                sum = numbers[i] + numbers[j]
                if sum == target:
                    return [i+1, j+1]
                if sum > target:
                    break
                j += 1
        return None
                

