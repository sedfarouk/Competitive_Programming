# 1347. Leetcode - Minimum Number Of Steps To Make Two Strings Anagram

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)

        missing = s_count - t_count

        return sum(missing.values())
