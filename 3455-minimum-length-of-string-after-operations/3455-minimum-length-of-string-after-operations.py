class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        ans = sum([x & 1 for x in cnt.values()])
        ans += len([x for x in cnt.values() if x % 2 == 0]) * 2
        return ans