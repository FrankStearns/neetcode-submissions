class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        speed = right
        while left <= right:
            mid = (left + right) // 2
            current = 0
            for pile in piles:
                current += math.ceil(pile / mid)
            if current <= h:
                speed = min(speed, mid)
                right = mid - 1
            else: 
                left = mid + 1
        return speed



        