class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        hashmap = Counter(s)

        sorted_freqs = sorted(hashmap.values(), reverse=True)

        for i in range(1, len(sorted_freqs)):
            while sorted_freqs[i] >= sorted_freqs[i-1] and sorted_freqs[i] != 0:
                sorted_freqs[i] -= 1
                deletions += 1
        
        return deletions
        