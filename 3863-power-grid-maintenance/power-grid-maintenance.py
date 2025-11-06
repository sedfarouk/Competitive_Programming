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
        non_op = [False] * c
        for t, st in queries:
            st = st - 1
            if t == 1:
                if not non_op[st]:
                    ans.append(st + 1)
                    continue

                heap = heaps[indices[st]]
                while heap and non_op[heap[0]]:
                    heappop(heap)
                    
                if heap: ans.append(heap[0] + 1)
                else: ans.append(-1)
            else:
                non_op[st] = True

        return ans


        