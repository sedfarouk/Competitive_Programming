class UnionFind:
    def __init__(self, n):
        self.par = [*range(n)]
        self.size = [1] * n

    def find(self, u):
        if u == self.par[u]:
            return u
        self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self, u, v):
        rootX = self.find(u)
        rootY = self.find(v)

        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX
        
        self.par[rootY] = rootX
        self.size[rootX] += self.size[rootY]

    def reset(self, u):
        self.par[u] = u
        self.size[u] = 1

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        uf.union(0, firstPerson)

        same_time = defaultdict(list)

        for u, v, t in meetings:
            same_time[t].append((u, v))

        for t in same_time:
            for x, y in same_time[t]:
                uf.union(x, y)

            for x, y in same_time[t]:
                if uf.find(x) != uf.find(0):
                    uf.reset(x)
                    uf.reset(y)

        return [i for i in range(n) if uf.find(i) == uf.find(0)]

        # DJIKSTRA-LIKE
        # graph = defaultdict(list)

        # for u, v, t in meetings:
        #     graph[u].append((t, v))  
        #     graph[v].append((t, u))   

        # for node in graph:
        #     graph[node].sort()

        # vis = [False] * n
        # queue = [(0, 0), (0, firstPerson)]
        # time = { i: float("inf") for i in range(n) }
        
        # while queue:
        #     t1, q = heappop(queue)
            
        #     if vis[q]:
        #         continue

        #     vis[q] = True
        #     i = bisect_left(graph[q], (t1, -1))

        #     for j in range(i, len(graph[q])):
        #         t2, nei = graph[q][j]

        #         if t2 >= t1 and t2 < time[nei] and not vis[nei]:
        #             time[nei] = t2
        #             heappush(queue, (t2, nei))

        # return [i for i in range(n) if vis[i]]
            

