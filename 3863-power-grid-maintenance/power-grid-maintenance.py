class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in connections:
            u -= 1; v -= 1
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u):
            stk = [u]

            while stk:
                st = stk.pop()

                for nei in graph[st]:
                    if not vis[nei]:
                        heappush(heaps[-1], nei)
                        indices[nei] = len(heaps) - 1
                        vis[nei] = True
                        stk.append(nei)

        indices = defaultdict(int)
        heaps = []
        vis = [False] * c
        for i in range(c):
            if not vis[i]:
                heaps.append([i])
                indices[i] = len(heaps) - 1
                vis[i] = True
                dfs(i)

        ans = []
        non_op = set()
        for t, st in queries:
            if t == 1:
                if st - 1 not in non_op:
                    ans.append(st)
                    continue
                heap = heaps[indices[st - 1]]
                while heap and heap[0] in non_op:
                    heappop(heap)
                if heap: ans.append(heap[0] + 1)
                else: ans.append(-1)
            else:
                non_op.add(st - 1)

        return ans


        