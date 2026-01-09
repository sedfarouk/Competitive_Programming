class Solution:
    def findOrder(self, n: int, pr: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inorder = [0] * n

        for u, v in pr:
            graph[v].append(u)
            inorder[u] += 1

        queue = deque([i for i in range(n) if inorder[i] == 0])
        ordering = []

        while queue:
            c = queue.popleft()

            for nei in graph[c]:
                inorder[nei] -= 1

                if inorder[nei] == 0:
                    queue.append(nei)

            ordering.append(c)

        return ordering if len(ordering) == n else []
