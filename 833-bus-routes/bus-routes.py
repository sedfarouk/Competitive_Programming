class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        n = len(routes)

        if source == target: return 0
        
        routes = [set(route) for route in routes]
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if len(routes[i].intersection(routes[j])) != 0:
                    graph[i].append(j)
                    graph[j].append(i)

        ans = 0
        st_nodes = [i for i in range(n) if source in routes[i]]
        queue = deque(st_nodes)
        vis = set(st_nodes)

        while queue:
            l = len(queue)

            for _ in range(l):
                bus = queue.popleft()

                if target in routes[bus]:
                    return ans + 1

                for nei in graph[bus]:
                    if nei in vis:
                        continue
                    vis.add(bus)
                    queue.append(nei)
            ans += 1

        return -1
                
        