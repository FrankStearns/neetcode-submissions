class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        needs = {}
        n = len(numbers)
        for i in range(n):
            if numbers[i] not in needs:
                needs[target - numbers[i]] = i
        for j in range(n):
            if numbers[j] in needs and needs[numbers[j]] != j:
                return [needs[numbers[j]] + 1, j + 1]

