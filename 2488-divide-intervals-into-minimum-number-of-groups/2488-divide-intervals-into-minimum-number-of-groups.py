class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # DIFFERENCE ARRAY (SWEEP LINE)
        arr = []

        for r, l in intervals:
            arr.append((r, 1))
            arr.append((l+1, -1))

        ans = curr = 0
        for x, diff in sorted(arr):
            curr += diff
            ans = max(ans, curr)
        return ans

        # HEAP

        # intervals.sort()
        # heap = [intervals[0][1]]

        # for r, l in intervals[1:]:
        #     if r > heap[0]:
        #         heappop(heap)
        #     heappush(heap, l)
        # return len(heap)
