class UnionFind:
    def __init__(self):
        self.parents = [*range(27)]
        self.size = [1]*26
        self.min = [*range(27)]

    def find(self, root):
        if self.parents[root]==root:
            return root
        self.parents[root] = self.find(self.parents[root])
        return self.parents[root] 

    def union(self, u, v):
        rootX, rootY = self.find(u), self.find(v)

        if rootX!=rootY:
            if self.size[rootX] > self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parents[rootX] = rootY
            self.min[rootY] = min(self.min[rootY], self.min[rootX])
            self.size[rootY] += self.size[rootX]

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        forest = UnionFind()

        for a, b in zip(s1, s2):
            ascii_a, ascii_b = ord(a)-ord('a'), ord(b)-ord('a')
            forest.union(ascii_a, ascii_b)

        ans = ""
        for ch in baseStr:
            f = forest.find(ord(ch)-ord('a'))
            s = chr(forest.min[f]+97)
            ans += s
        return ans