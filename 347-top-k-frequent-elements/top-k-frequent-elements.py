class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        freqs = Counter(nums)
        cntSort = [[] for _ in range(max(freqs.values()) + 1)]

        for num, freq in freqs.items():
            cntSort[freq].append(num)

        ans = []
        for i in range(len(cntSort) - 1, -1, -1):
            ans.extend(cntSort[i])

            if len(ans) == k:
                return ans