class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashmap = defaultdict(int)
        maxx = -1

        for i in range(len(s)):
            if s[i] in hashmap:
                maxx = max(maxx, i-hashmap[s[i]]-1)
            else:
                hashmap[s[i]] = i
        
        return maxx