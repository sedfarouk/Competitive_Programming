class UnionFind:
    def __init__(self, accounts):
        self.parents = {}
        self.name = {}
        self.size = {}
        
        for acct in accounts:
            for email in acct[1:]:
                self.parents[email] = email
                self.name[email] = acct[0]
                self.size[email] = 1

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(accounts)
        
        for acct in accounts:
            emails = acct[1:]
            for i in range(1, len(emails)):
                uf.union(emails[i], emails[i-1])

        user_emails, users = defaultdict(list), []
        for key in uf.parents.keys():
            user_emails[uf.find(key)].append(key) 
            
        for val in user_emails.values():
            users.append([uf.name[val[0]]] + sorted(val))
        
        return users
        
