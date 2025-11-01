class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        need = []
        for num in nums:
            pf = 1
            x = num
            for i in range(2, int(num ** 0.5) + 1):
                cnt = 0
                while x % i == 0:
                    x //= i
                    cnt += 1

                if cnt % 2: pf *= i
            if x > 1:
                pf *= x
            need.append(pf)

        ans = [0]
        def dfs(node, par):
            ans[-1] += mp[need[node]]
            mp[need[node]] += 1
            
            for nei in graph[node]:
                if nei == par:
                    continue
                dfs(nei, node)
            mp[need[node]] -= 1

        mp = defaultdict(int)
        dfs(0, -1)
        return ans[-1]
            
            