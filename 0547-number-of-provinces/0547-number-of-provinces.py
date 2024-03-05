class UnionFind:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.size = [1]*n

    def find(self, node):
        if self.roots[node]==node:
            return node
        
        self.roots[node] = self.find(self.roots[node])
        return self.roots[node]

    def union(self, u, v):
        rootX = self.find(u)
        rootY = self.find(v)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.roots[rootY] = rootX
            
            elif self.size[rootX] < self.size[rootY]:
                self.roots[rootX] = rootY

            else:
                self.roots[rootX] = rootY
                self.size[rootX] += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        forest = UnionFind(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    forest.union(i, j)

        return len(set([forest.find(i) for i in range(len(isConnected))]))

        

        # graph = defaultdict(list)
        # visited = set()

        # for i in range(len(isConnected)):
        #     for j in range(len(isConnected)):
        #         if isConnected[i][j]==1:
        #             if i!=j:
        #                 graph[i+1].append(j+1)

        # def dfs(node):
        #     visited.add(node)

        #     for neighbour in graph[node]:
        #         if neighbour not in visited:
        #             dfs(neighbour)

        # count = 0
        # for node in range(1, len(isConnected)+1):
        #     if node not in visited:
        #         dfs(node)
        #         count += 1
        # return count