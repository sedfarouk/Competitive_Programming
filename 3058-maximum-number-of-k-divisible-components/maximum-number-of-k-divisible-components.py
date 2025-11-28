class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        ans = 0
        stack = [(0, -1, 0)]

        while stack:
            st, par, state = stack.pop()
            
            if not state:
                stack.append((st, par, 1))
                for nei in tree[st]:
                    if nei != par:
                        stack.append((nei, st, 0))
            
            else:
                for nei in tree[st]:
                    if nei != par:
                        values[st] += values[nei]

                ans += int(values[st] % k == 0)

        return ans
