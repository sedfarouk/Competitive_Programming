class UnionFind:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.size = [1]*n

    def find(self, root):
        member = root

        while self.roots[root] != root:
            root = self.roots[root]

        while member != root:
            node = self.roots[member]
            self.roots[member] = root
            member = node
        return root

    def union(self, u, v):
        rootX, rootY = self.find(u), self.find(v)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.roots[rootY] = rootX

            elif self.size[rootX] < self.size[rootY]:
                self.roots[rootX] = rootY
            
            else:
                self.roots[rootX] = self.roots[rootY]
                self.size[rootX] += 1

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        forest = UnionFind(n)

        for edge in edges:
            forest.union(edge[0], edge[1])

        return forest.find(source)==forest.find(destination)
        
        # graph = defaultdict(list)
        
        # for edge in edges:
        #     graph[edge[0]].append(edge[1])
        #     graph[edge[1]].append(edge[0])

            
        # def dfs(vertex, visited):
        #     if vertex==destination:
        #         return True
            
        #     visited.add(vertex)
            
        #     for neighbour in graph[vertex]:
        #         if neighbour not in visited:
        #             found = dfs(neighbour, visited)
                    
        #             if found:
        #                 return True
        #     return False
        
        # visited = set()
        
        # return dfs(source, visited)

        
        
            
            
        