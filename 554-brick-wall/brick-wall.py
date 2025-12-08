class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        freqs = defaultdict(lambda : n)
        ans = n

        for row in wall:
            curr = 0
            for i in range(len(row) - 1):
                curr += row[i]
                freqs[curr] -= 1
                ans = min(ans, freqs[curr])

        return ans

        