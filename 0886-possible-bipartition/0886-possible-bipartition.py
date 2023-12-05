class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {i:[] for i in range(1, n+1)}

        for edge in dislikes:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        color = [0]*n
        ans = True

        def dfs(node):
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    color[neighbour-1] = color[node-1] * -1
                    dfs(neighbour)

                else:
                    nonlocal ans
                    ans = ans and color[node-1]!=color[neighbour-1]

        for node in range(1, n+1):
            if node not in visited:
                color[node-1] = 1
                dfs(node)

        return ans


        