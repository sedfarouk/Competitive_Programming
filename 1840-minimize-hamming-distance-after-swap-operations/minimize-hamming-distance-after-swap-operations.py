class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        g = defaultdict(list)

        for u, v in allowedSwaps:
            g[u].append(v); g[v].append(u)

        vis = set()
        def bfs(u):
            q = deque([u])
            cntT, cntS = Counter(), Counter()
            vis.add(u)

            while q:
                x = q.popleft()
                cntT[target[x]] += 1; cntS[source[x]] += 1

                for nei in g[x]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append(nei)

            cntRes = cntT - cntS
            res = sum([abs(x) for x in cntRes.values()])
            return res

        ans = 0
        for u in range(len(source)):
            if u not in vis: ans += bfs(u)
        
        return ans
