class UnionFind:
    def __init__(self):
        self.parents = [*range(27)]
        self.size = [1]*(26)

    def find(self, root):
        if self.parents[root]==root:
            return root
        self.parents[root] = self.find(self.parents[root])
        return self.parents[root]

    def union(self, u, v):
        rootX, rootY = self.find(u), self.find(v)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parents[rootX] = rootY
            self.size[rootY] += self.size[rootX]


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()

        for eq in equations:
            asc_a, asc_b = ord(eq[0])-ord('a'), ord(eq[-1])-ord('a')
            if eq[1]=="=":
                uf.union(asc_a, asc_b)

        for eq in equations:
            asc_a, asc_b = ord(eq[0])-ord('a'), ord(eq[-1])-ord('a')
            if eq[1]=="!" and uf.find(asc_a)==uf.find(asc_b):
                return False

        return True
            