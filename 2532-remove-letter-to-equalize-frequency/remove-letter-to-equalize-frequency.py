class Solution:
    def equalFrequency(self, word: str) -> bool:
        freqs = Counter(word)
        u = set(freqs.values())

        if len(u) > 2:
            return False

        mx, mn = max(u), min(u)
        fmn, fmx = list(freqs.values()).count(mn), list(freqs.values()).count(mx)

        if mn == 1 and (fmn == 1 or fmn == len(freqs)):
            return True

        if mx - mn == 1 and fmx == 1 and fmn == len(freqs) - 1:
            return True

        return len(freqs) == 1