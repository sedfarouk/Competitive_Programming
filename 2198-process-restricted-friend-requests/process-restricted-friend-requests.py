class UnionFind:
    def __init__(self, n, restrictions):
        self.par = [*range(n)]
        self.members = [set([i]) for i in range(n)]
        self.enemies = [set() for i in range(n)]
        self.size = [1] * n

        for u, v in restrictions:
            self.enemies[u].add(v)
            self.enemies[v].add(u)

    def find(self, root):
        if self.par[root] == root:
            return root
        self.par[root] = self.find(self.par[root])
        return self.par[root]

    def union(self, u, v):
        rootX, rootY = self.find(u), self.find(v)

        if rootX == rootY:
            return True

        if self.enemies[rootX].intersection(self.members[rootY]):
            return False

        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX

        self.par[rootY] = rootX
        self.enemies[rootX] |= self.enemies[rootY]
        self.members[rootX] |= self.members[rootY]
        self.size[rootX] += self.size[rootY]

        return True


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UnionFind(n, restrictions)

        ans = []
        for u, v in requests:
            ans.append(uf.union(u, v))

        return ans

        
        