class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]

        graph = defaultdict(list)
        incoming = [0]*n

        for u, v in edges:
            graph[u] += [v]
            graph[v] += [u]
            incoming[u] += 1
            incoming[v] += 1

        queue = deque([i for i in range(n) if incoming[i]==1])
        while n > 2:
            level = len(queue)
            n -= len(queue)

            for _ in range(level):
                node = queue.popleft()
                for nei in graph[node]:
                    incoming[nei] -= 1

                    if incoming[nei]==1:
                        queue.append(nei)

        return queue


            
            


        