class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def dfs(root, par):
            for nei in tree[root]:
                if nei != par:
                    values[root] += dfs(nei, root)
                    
            ans[-1] += int(values[root] % k == 0)
            return values[root]

        ans = [0]
        dfs(0, -1)
        return ans[-1]