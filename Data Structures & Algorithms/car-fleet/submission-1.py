class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPosition, sortedSpeed = zip(*sorted(zip(position, speed),reverse=True))
        current = (target - sortedPosition[0])/sortedSpeed[0]
        out = 1
        for i in range(1,len(sortedPosition)):
            timeToTarget = (target - sortedPosition[i])/sortedSpeed[i]
            if timeToTarget <= current:
                continue
            else:
                current = timeToTarget
                out += 1
        return out
