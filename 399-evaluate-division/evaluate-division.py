class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        graph = defaultdict(list)

        for i in range(n):
            u, v = equations[i]
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))

        def eval_dfs(src, target):
            stack = [(src, 1)]
            vis = set([src])

            while stack:
                u, val = stack.pop()

                if u == target:
                    return val

                for nei, f in graph[u]:
                    if nei not in vis:
                        stack.append((nei, val * f))
                        vis.add(nei)

            return -1.0

        res = []
        for u, v in queries:
            if u not in graph or v not in graph:
                res.append(-1.0)
            else:
                res.append(eval_dfs(u, v))

        return res
