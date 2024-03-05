class UnionFind:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.size = [1]*n

    def find(self, root):
        member = root

        while root != self.roots[root]:
            root = self.roots[root]

        while member != root:
            parent = self.roots[member]
            self.roots[member] = root
            member = parent
        return root

    def union(self, u, v):
        rootX, rootY = self.find(u), self.find(v)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.roots[rootY] = rootX

            elif self.size[rootX] < self.size[rootY]:
                self.roots[rootX] = rootY

            else:
                self.roots[rootX] = rootY
                self.size[rootX] += 1
            

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        forest = UnionFind(len(edges))
        ans = [-1, -1]

        for edge in edges:
            if forest.find(edge[0]-1)==forest.find(edge[1]-1):
                ans = [edge[0], edge[1]]
            forest.union(edge[0]-1, edge[1]-1)

        return ans
        