class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            graph[eq[0]].append((eq[1], values[i]))
            graph[eq[1]].append((eq[0], 1/values[i]))

        def find(u, v):
            if u not in graph or v not in graph:
                return -1.0

            vis = set([u])
            q = deque([(u, 1)])
            while q:
                x, c = q.popleft()

                if x==v:
                    return c

                for nei, w in graph[x]:
                    if nei not in vis:
                        q.append((nei, c*w))
                        vis.add(nei)
            
            return -1.0

        ans = []
        for query in queries:
            ans.append(find(query[0], query[1]))
        return ans