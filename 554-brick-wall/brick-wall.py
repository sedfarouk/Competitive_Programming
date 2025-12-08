class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        freqs = defaultdict(int)
        interceptions = 0

        for row in wall:
            curr = 0
            for i in range(len(row) - 1):
                curr += row[i]
                freqs[curr] += 1
        
        for v in freqs.values():
            interceptions = max(interceptions, v)

        return n - interceptions

        