class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i,n in enumerate(nums):
            count[n] += 1
        
        sorted_keys = sorted(count, key=count.get, reverse=True)
        return sorted_keys[:k];
    