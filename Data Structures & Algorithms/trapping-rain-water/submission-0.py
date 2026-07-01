class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        lmax = [height[0]]
        rmax = [height[n-1]]
        for i in range(1,n):
            lmax.append(max(height[i],lmax[-1]))
            rmax.append(max(height[n-i-1],rmax[-1]))
        rmax = rmax[::-1]
        for i in range(n):
            water += min(lmax[i],rmax[i]) - height[i]
        return water
        
