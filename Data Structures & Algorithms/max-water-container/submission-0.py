class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            left = heights[i]
            right = heights[j]
            area = min(left,right)*(j-i)
            if area > out:
                out = area
            if left < right:
                i += 1
            if right <= left:
                j -= 1
        return out