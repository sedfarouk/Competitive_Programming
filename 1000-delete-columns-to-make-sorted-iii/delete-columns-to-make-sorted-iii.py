class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        max_lengths = [1] * m

        for i in range(m):
            for j in range(i):
                if all(strs[k][i] >= strs[k][j] for k in range(n)):
                    max_lengths[i] = max(max_lengths[i], max_lengths[j] + 1)

        return m - max(max_lengths)



