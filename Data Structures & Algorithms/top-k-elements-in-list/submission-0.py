class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        topk = [item for item, n in n.most_common(k)]
        return topk  
            