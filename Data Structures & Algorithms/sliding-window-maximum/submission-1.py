class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []

        for i in range(k):
            heapq.heappush(max_heap, -nums[i])
        out = [-max_heap[0]]
        
        for j in range(k,len(nums)):
            heapq.heappush(max_heap, -nums[j])
            if nums[j-k] == -max_heap[0]:
                tempset = set(nums[j-k+1:j+1])
                while -max_heap[0] not in tempset:
                    heapq.heappop(max_heap)
            out.append(-max_heap[0])
        
        return out