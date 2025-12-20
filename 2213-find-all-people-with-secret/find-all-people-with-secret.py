class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)

        for u, v, t in meetings:
            graph[u].append((t, v))  
            graph[v].append((t, u))      

        for node in graph:
            graph[node].sort()

        vis = [False] * n
        queue = [(0, 0), (0, firstPerson)]
        time = { i: float("inf") for i in range(n) }
        
        while queue:
            t1, q = heappop(queue)
            
            if vis[q]:
                continue

            vis[q] = True
            i = bisect_left(graph[q], (t1, -1))
            
            for j in range(i, len(graph[q])):
                t2, nei = graph[q][j]

                if t2 >= t1 and t2 < time[nei] and not vis[nei]:
                    time[nei] = t2
                    heappush(queue, (t2, nei))

        return [i for i in range(n) if vis[i]]
            

