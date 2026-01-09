class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        n = len(routes)

        if source == target: return 0

        routes = [set(route) for route in routes]
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if len(routes[i] & routes[j]) > 0:
                    graph[i].append(j)
                    graph[j].append(i)

        queue = deque([i for i in range(n) if source in routes[i]])
        vis = [False] * n

        for node in queue: vis[node] = True

        ans = 0
        
        while queue:
            l = len(queue)
            ans += 1

            for _ in range(l):
                route = queue.popleft()

                if target in routes[route]:
                    return ans

                for nei in graph[route]:
                    if not vis[nei]:
                        queue.append(nei)
                        vis[nei] = True
            
        return -1