class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [intervals[0][1]]

        for r, l in intervals[1:]:
            if r > heap[0]:
                heappop(heap)
            heappush(heap, l)
        return len(heap)
