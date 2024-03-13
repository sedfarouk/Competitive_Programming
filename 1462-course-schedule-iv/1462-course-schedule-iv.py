class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[float('inf')] * numCourses for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a][b] = 1

        for i in range(numCourses):
            graph[i][i] = 0
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        ans = [False] * len(queries)
        i = 0
        for u, v in queries:
            if graph[u][v] != float('inf'):
                ans[i] = True
            i += 1
        return ans