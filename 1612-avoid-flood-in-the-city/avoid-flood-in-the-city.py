class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        filled = defaultdict(int)
        empty = SortedList()
        ans = [-1] * len(rains) 

        for idx, r in enumerate(rains):
            if r > 0:
                if r in filled:
                    if not empty or empty[-1] < filled[r]:
                        return []
                    x = empty.bisect_right(filled[r])
                    ans[empty.pop(x)] = r
                filled[r] = idx
            else:
                empty.add(idx)

        while empty:
            ans[empty.pop()] = 1

        return ans

