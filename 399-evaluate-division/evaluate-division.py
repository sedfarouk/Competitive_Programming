class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            x, y = equations[i]
            v1, v2 = values[i], 1 / values[i]

            graph[x].append((v1, y))
            graph[y].append((v2, x))

        def dfs(curr, target, val):
            if curr == target:
                return val

            for v, nei in graph[curr]:
                if nei in vis:
                    continue
        
                vis.add(nei)
                res = dfs(nei, target, val * v)
                if res != -1.0:
                    return res

            return -1.0

        ans = []
        for st, end in queries:
            if st not in graph or end not in graph:
                ans.append(-1.0)
            else:
                vis = set([st])
                ans.append(dfs(st, end, 1))

        return ans