class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        sorted_keys = sorted(list(hashmap.items()), key = lambda x:x[1], reverse=True)
        return [sorted_keys[i][0] for i in range(k)]

