class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        h = []
        for num, f in cnt.items():
            if len(h) < k:
                heappush(h, (f, num))

            elif f > h[0][0]:
                heapreplace(h, (f, num))

        return [x[1] for x in h]


