class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_nodes = defaultdict(list)
        out_degree = [0]*len(graph)

        for i in range(len(graph)):
            for node in graph[i]:
                adj_nodes[node].append(i) 
                out_degree[i] += 1

        ans = []
        queue = deque([i for i in range(0, len(graph)) if out_degree[i]==0])

        while queue:
            q = queue.popleft()

            for nei in adj_nodes[q]:
                out_degree[nei] -= 1

                if out_degree[nei]==0:
                    queue.append(nei)

            ans.append(q)
        return sorted(ans)
            
            

