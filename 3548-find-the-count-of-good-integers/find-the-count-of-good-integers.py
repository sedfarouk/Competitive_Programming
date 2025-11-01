class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half = (n + 1) // 2
        seen = set()
        ans = 0

        for num in range(10 ** (half - 1), 10 ** half):
            v = str(num) + str(num)[::-1][n % 2:]

            if int(v) % k == 0:
                val = ''.join(sorted(v))

                if val in seen: 
                    continue

                mp = Counter(val)
                seen.add(val)
                ans += (((n - mp['0']) * factorial(n - 1)) // prod([factorial(x) for x in mp.values()]))
        
        return ans


        