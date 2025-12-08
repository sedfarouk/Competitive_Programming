class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        freqs = defaultdict(int)
        ans = len(wall)

        for row in wall:
            curr = 0
            for i in range(len(row) - 1):
                curr += row[i]
                freqs[curr] += 1
        
        for v in freqs.values():
            ans = min(ans, len(wall) - v)

        return ans

        