class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        hashmap = Counter(s)
        seen = set()

        for key, freq in hashmap.items():
            while freq > 0  and freq in seen:
                freq -= 1
                deletions += 1
            seen.add(freq)
        
        return deletions
        