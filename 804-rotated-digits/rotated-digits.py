class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = [0, 1, 2, 5, 6, 8, 9]

        def backtrack(num):
            ans = 0
            for d in valid:
                new = num * 10 + d
                if new <= n:
                    ans += backtrack(new) + any(x for x in str(new) if x not in ('0', '1', '8'))
            
            return ans

        res = 0
        for i in range(1, 7):
            if valid[i] <= n: res += backtrack(valid[i]) + int(valid[i] not in (0, 1, 8))

        return res
