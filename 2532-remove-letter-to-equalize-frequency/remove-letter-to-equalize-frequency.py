class Solution:
    def equalFrequency(self, word: str) -> bool:
        freqs = list(Counter(word).values())
        u = set(freqs)

        if len(u) > 2:
            return False

        mn, mx = min(u), max(u)
        fmn, fmx = freqs.count(mn), freqs.count(mx)
        
        if mn == 1 and (fmn == 1 or fmn == len(freqs)):
            return True

        if mx - mn == 1 and fmx == 1 and fmn == len(freqs) - 1:
            return True
        
        return len(u) == len(freqs) == 1
