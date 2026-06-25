class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum = 0
        for i in range(1,max(heights)+1):
            current = 0
            for j in range(len(heights)):
                if heights[j] - i < 0:
                    current = 0
                else: 
                    current += i
                    if current > maximum:
                        maximum = current
        return maximum

