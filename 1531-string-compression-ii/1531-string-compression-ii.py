class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(idx, prev, prev_cnt, k):
            if k < 0: return float("inf")
            if idx==len(s): return 0

            delete = dp(idx+1, prev, prev_cnt, k-1)
            if s[idx]==prev:
                keep = dp(idx+1, prev, prev_cnt+1, k)

                if prev_cnt in [1, 9, 99]:
                    keep += 1
            
            else:
                keep = dp(idx+1, s[idx], 1, k) + 1
            
            return min(delete, keep)

        return dp(0, "", 0, k)


