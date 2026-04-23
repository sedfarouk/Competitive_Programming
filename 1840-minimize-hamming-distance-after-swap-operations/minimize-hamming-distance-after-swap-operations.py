class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        par = {i:i for i in range(n)}
        sz = [1] * n
        vals = {i: Counter([source[i]]) for i in range(n)}

        def find(u):
            if par[u] == u:
                return u
            par[u] = find(par[u])
            return par[u]

        def union(u, v):
            ru, rv = find(u), find(v)

            if ru != rv:
                if sz[ru] > sz[rv]:
                    par[rv] = ru
                    sz[ru] += sz[rv]
                    vals[ru].update(vals[rv])
                else:
                    par[ru] = rv
                    sz[rv] += sz[ru]
                    vals[rv].update(vals[ru])

        for u, v in allowedSwaps:
            union(u, v)
        
        ans = 0
        for i in range(n):
            p = find(i)
            if target[i] not in vals[p]:
                ans += 1
            else:
                vals[p][target[i]] -= 1

                if vals[p][target[i]] == 0:
                    del vals[p][target[i]]

        return ans
