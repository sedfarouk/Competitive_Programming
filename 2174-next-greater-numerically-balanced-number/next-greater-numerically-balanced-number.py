class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n = str(n)

        def next_greater(perm, target):
            ss = SortedList(perm)

            break_point = -1
            for i in range(len(target)):
                if ss[-1] < target[i]: break
                if ss[-1] > target[i]: break_point = i
                if target[i] in ss: ss.remove(target[i])
                else: break

            if break_point == -1: return float("inf")

            res = []
            ss = SortedList(perm)
            for i in range(break_point):
                res.append(target[i])
                ss.remove(target[i])

            idx = ss.bisect_right(target[break_point])
            res.append(ss[idx])
            ss.pop(idx)

            res.extend(ss)
            return int("".join(res))
        
        ans = float("inf")
        for mask in range((1 << 9) + 1):
            d = []
            for i in range(9):
                if mask & (1 << i):
                    d.extend([str(i + 1)] * (i + 1))

            if len(d) < len(n): continue
            elif len(d) > len(n): ans = min(ans, int("".join(sorted(d))))
            else: ans = min(ans, next_greater(d, n))

        return ans

            

