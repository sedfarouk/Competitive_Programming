class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        def djikstra(source):
            dist = [float("inf")]*n
            dist[source] = 0
            heap = [(0, source)]

            while heap:
                dis, node = heappop(heap)
                
                if dist[node]==dis:
                    for weight, nei in graph[node]:
                        if weight + dis < dist[nei]:
                            dist[nei] = weight + dis
                            heappush(heap, (dist[nei], nei))
            return dist

        dist0 = djikstra(0)
        dist1 = djikstra(n-1)

        ans = []
        if dist0[n-1]==float("inf"): return [False]*len(edges)
        
        for u, v, w in edges:
            ans.append(dist0[u] + w + dist1[v] == dist0[n-1] or dist0[v]+w+dist1[u]==dist0[n-1])
        return ans 


            
