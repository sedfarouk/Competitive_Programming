class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def dfs(root, par):
            if root in memo:
                return memo[root]

            for nei in tree[root]:
                if nei != par:
                    values[root] += dfs(nei, root)

            ans[-1] += int(values[root] % k == 0)
            memo[root] = values[root]
            return memo[root]

        ans = [0]
        memo = {}
        dfs(0, -1)
        return ans[-1]