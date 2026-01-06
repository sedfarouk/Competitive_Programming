class Solution:
    def minMoves(self, balance: List[int]) -> int:
        ans = ptr = 0
        n = len(balance)

        for i in range(n):
            if balance[i] < 0:
                ptr = i
                break

        d = 1
        while ((ptr - d) % n) != ptr and balance[ptr] < 0:
            l, r = (ptr - d) % n, (ptr + d) % n
            
            ans += min(abs(balance[ptr]), balance[l]) * abs(ptr - (ptr - d))
            balance[ptr] += balance[l]
            balance[l] = 0

            if balance[ptr] >= 0:
                return ans

            ans += min(abs(balance[ptr]), balance[r]) * abs(ptr - (ptr + d))
            balance[ptr] += balance[r]
            balance[r] = 0

            d += 1
                
        return ans if balance[ptr] >= 0 else -1