class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)

        missing = (s_count - t_count) + (t_count - s_count)

        return sum(missing.values())

        # s_letters, t_letters = [0]*26, [0]*26
        # ans = 0

        # for i in s:
        #     s_letters[ord(i)-ord('a')] += 1

        # for i in t:
        #     t_letters[ord(i)-ord('a')] += 1
        
        # for i in range(26):
        #     ans += abs(s_letters[i]-t_letters[i])
        
        # return ans
        
