class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = ((10**9)+7)
        graph = {i:[] for i in range(n)}

        for u, v, t in roads:
            graph[u] += [(t, v)]
            graph[v] += [(t, u)]

        heap = [(0, 0)]
        dist = [float("inf")]*n
        dist[0] = 0

        while heap:
            time, node = heappop(heap)

            for nei_time, nei_node in graph[node]:
                new_time = nei_time + time
                
                if new_time < dist[nei_node]:
                    dist[nei_node] = new_time
                    heappush(heap, (new_time, nei_node)) 
        
        @lru_cache(None)
        def dp(node, time):
            if node==0:
                return 1

            res = 0
            for nei in graph[node]:
                if time + nei[0] + dist[nei[1]] <= dist[-1]:
                    res += dp(nei[1], time + nei[0])

            return res
        return dp(n-1, 0) % MOD

            
               
             
                
        
