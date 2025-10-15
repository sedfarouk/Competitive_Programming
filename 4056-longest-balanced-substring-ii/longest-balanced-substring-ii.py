class Solution:
    def countTwo(self, s, x, y):
        h = defaultdict(int)
        h[0] = -1
        res = c = 0
        for i in range(len(s)):
            if s[i] == x: c += 1
            elif s[i] == y: c -= 1
            else: h = defaultdict(int); h[0] = i; c = 0

            if c in h: res = max(res, i - h[c])
            else: h[c] = i

        return res 

    def longestBalanced(self, s: str) -> int:
        ans = cnt = 1
        n = len(s)

        for i in range(1, n):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1

        ans = max(ans, cnt)
        ans = max(ans, self.countTwo(s, 'a', 'b'), self.countTwo(s, 'b', 'c'), self.countTwo(s, 'a', 'c'))

        h = defaultdict(int)
        h[0] = -1
        cnt = 0
        for i in range(n):
            if s[i] == 'a': cnt += 1
            elif s[i] == 'b': cnt += 10 ** 6 - 1
            else: cnt -= 10 ** 6

            if cnt in h: ans = max(ans, i - h[cnt])
            else: h[cnt] = i

        return ans
        