class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        heap = [(-val, key) for key, val in hashmap.items()]
        heapify(heap)
        ans = []

        for _ in range(k):
            freq, val = heappop(heap)
            ans.append(val)
            
        return ans

