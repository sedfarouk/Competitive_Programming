class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        freqs = Counter(nums)
        cntSort = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqs.items():
            cntSort[freq].append(num)

        ans = []
        while len(ans) < k:
            ans.extend(cntSort.pop())

        return ans
