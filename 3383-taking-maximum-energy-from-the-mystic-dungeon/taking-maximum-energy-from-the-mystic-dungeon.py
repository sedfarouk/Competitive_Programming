class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = float("-inf")
        n = len(energy)
        
        for i in range(n - 1, n - k - 1, -1):
            curr = 0
            end = i

            while end >= 0:
                curr += energy[end]
                ans = max(ans, curr)
                end -= k

        return ans



