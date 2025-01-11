class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s): return False
        return len([x for x in Counter(s).values() if x % 2]) <= k