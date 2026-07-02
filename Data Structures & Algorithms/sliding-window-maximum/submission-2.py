class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        out = []
        for i in range(len(nums)):
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)
            while deq[0] < i - k + 1:
                deq.popleft()
            if i < k-1:
                continue
            out.append(nums[deq[0]])
        return out