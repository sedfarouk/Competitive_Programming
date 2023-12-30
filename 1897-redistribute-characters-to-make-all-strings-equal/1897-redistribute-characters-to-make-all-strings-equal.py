class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hashmap = defaultdict(int)

        for word in words:
            for ch in word:
                hashmap[ch] += 1

        for val in hashmap.values():
            if val%len(words)!=0:
                return False
        return True