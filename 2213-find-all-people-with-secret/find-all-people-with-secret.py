class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)

        for u, v, t in meetings:
            graph[u].append((t, v))  
            graph[v].append((t, u))      

        for node in graph:
            graph[node].sort()

        vis = set()
        queue = [(0, 0), (0, firstPerson)]
        time = { i: float("inf") for i in range(n) }
        
        while queue:
            t1, q = heappop(queue)
            
            if q not in vis:
                vis.add(q)

            for t2, nei in graph[q]:
                if t2 >= t1 and t2 < time[nei] and nei not in vis:
                    time[nei] = t2
                    heappush(queue, (t2, nei))

        return list(vis)
            

