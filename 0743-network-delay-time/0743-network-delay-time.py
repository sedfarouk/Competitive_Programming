class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2], time[1]))

        dist = [float("inf") for _ in range(n+1)]
        dist[0] = dist[k] = 0
        heap = [(0, k)]
        
        while heap:
            dis, node = heappop(heap)
            
            for nei in graph[node]:
                edgeWeight = nei[0]
                adjNode = nei[1]
                
                if dis + edgeWeight < dist[adjNode]:
                    dist[adjNode] = dis + edgeWeight
                    heappush(heap, (dist[adjNode], adjNode))

        for x in dist:
            if x==float("inf"):
                return -1
        return max(dist)
        
        
        