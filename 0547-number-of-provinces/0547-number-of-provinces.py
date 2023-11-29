class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    if i!=j:
                        graph[i+1].append(j+1)

        def dfs(node):
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        count = 0
        for node in range(1, len(isConnected)+1):
            if node not in visited:
                dfs(node)
                count += 1
        return count