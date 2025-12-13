class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # DJIKSTRA ALGO (TLE NOW)
        # dist = [float("inf")] * n
        # dist[src] = 0

        # graph = defaultdict(list)
        # for u, v, w in flights:
        #     graph[u].append((v, w))

        # queue = [(0, src, k + 1)]
        # while queue:
        #     curr_d, node, steps = heappop(queue)

        #     if node == dst:
        #         return curr_d

        #     for nei, w in graph[node]:
        #         new_d = curr_d + w

        #         if steps > 0 and new_d < dist[nei]:
        #             heappush(queue, (new_d, nei, steps - 1))
        # return -1

        # BELLMAN-FORD ALGO
        dist = [float("inf")] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp = dist[:]
            for u, v, w in flights:
                curr_dist = dist[u] + w

                if dist[u] != float("inf") and curr_dist < temp[v]:
                    temp[v] = curr_dist
            dist = temp 

        return dist[dst] if dist[dst] != float("inf") else -1
        
            
        