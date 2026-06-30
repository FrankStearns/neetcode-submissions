class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        out = [0] * n
        for i in range(n):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                print(j)
                out[j] = i - j
            stack.append(i)
        return out
            