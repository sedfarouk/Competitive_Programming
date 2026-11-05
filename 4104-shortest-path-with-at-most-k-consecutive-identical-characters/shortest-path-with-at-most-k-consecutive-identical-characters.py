class Solution:
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            d, u, cnt = heappop(pq)

            if d != dist[u][cnt]:
                continue

            if u == n - 1:
                return d

            for v, w in graph[u]:
                nc = cnt + 1 if labels[u] == labels[v] else 1

                if nc > k:
                    continue

                nd = d + w

                # Check whether an existing state dominates this one.
                if any(dist[v][c] <= nd for c in range(1, nc + 1)):
                    continue

                # Remove states dominated by the new state.
                for c in range(nc, k + 1):
                    if dist[v][c] >= nd:
                        dist[v][c] = float('inf')

                dist[v][nc] = nd
                heappush(pq, (nd, v, nc))

        return -1
