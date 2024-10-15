class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def transform(num):
            cnt = 0
            while num != 1:
                if num % 2 == 0:
                    num //= 2
                else:
                    num = 3 * num + 1
                cnt += 1
            return cnt

        hmap = {}
        for x in range(lo, hi+1):
            hmap[x] = transform(x)

        vals = sorted([x for x in hmap.keys()], key=lambda x:(hmap[x], x))
        return vals[k-1]