class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0]*len(graph)
        visited = set()
        ans = True

        def dfs(node):
            nonlocal ans
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    color[nei] = color[node] * -1
                    dfs(nei)
                
                else:
                    ans = ans and color[node]!=color[nei]

        for i in range(len(graph)):
            if i not in visited:
                color[i] = 1
                dfs(i)

        return ans