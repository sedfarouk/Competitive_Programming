class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((w, v))

        queue = [(0, 0, 1)]
        dist = [[float("inf")] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        while queue:
            w, q, d = heappop(queue)

            for weight, nei in graph[q]:
                nw = w + weight
                nd = 1 if labels[q] != labels[nei] else (d + 1)

                if nd <= k and nw < dist[nei][nd]:
                    dist[nei][nd] = nw
                    heappush(queue, (nw, nei, nd))

        mn = min(dist[-1])
        return mn if mn != float("inf") else -1