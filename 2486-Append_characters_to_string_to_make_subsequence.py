#2486. Leetcode - Append Characters to String to Make Subsequence

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tp, sp = 0, 0

        while tp < len(t) and sp < len(s):
            if t[tp] != s[sp]:
                sp+=1
            else:
                tp+=1
                sp+=1
        return len(t)-tp
