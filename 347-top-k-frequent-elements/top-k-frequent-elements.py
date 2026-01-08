class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        n = len(nums)

        buckets = [[] for _ in range(n + 1)]
        for num, f in cnt.items():
            buckets[f].append(num)

        flat_list = [item for bucket in buckets for item in bucket]
        return flat_list[::-1][:k]
        
        # h = []
        # for num, f in cnt.items():
        #     if len(h) < k:
        #         heappush(h, (f, num))

        #     elif f > h[0][0]:
        #         heapreplace(h, (f, num))

        # return [x[1] for x in h]


