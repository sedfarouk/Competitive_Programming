class Solution:
    def minMoves(self, balance: List[int]) -> int:
        ans = ptr = 0
        n = len(balance)

        for i in range(n):
            if balance[i] < 0:
                ptr = i
                break

        vis = vis = set([ptr])
        l, r = ptr - 1, ptr + 1
        while l % n not in vis and balance[ptr] < 0:
            ans += min(abs(balance[ptr]), balance[l % n]) * abs(ptr - l)
            balance[ptr] += balance[l % n]
            balance[l % n] = 0

            if balance[ptr] >= 0:
                return ans

            ans += min(abs(balance[ptr]), balance[r % n]) * abs(ptr - r)
            balance[ptr] += balance[r % n]
            balance[r % n] = 0

            vis.add(l % n); vis.add(r % n)
            l, r = l - 1, r + 1
                
        return ans if balance[ptr] >= 0 else -1