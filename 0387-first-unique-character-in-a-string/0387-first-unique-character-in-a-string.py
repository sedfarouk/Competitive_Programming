class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = Counter(s)

        for key, val in hashmap.items():
            if val==1:
                return s.index(key)
        return -1