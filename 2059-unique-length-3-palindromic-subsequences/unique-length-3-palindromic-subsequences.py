class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        freq = Counter(s)
        prefCnt = defaultdict(int)
        seen = set()
        ans = 0

        for i in range(len(s)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if prefCnt[c] and freq[c] - prefCnt[c] - (s[i] == c):
                    curr = c + s[i]
                    if curr not in seen:
                        ans += 1
                        seen.add(curr)

            prefCnt[s[i]] += 1

        return ans

        