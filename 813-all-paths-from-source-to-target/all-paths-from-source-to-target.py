class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        solns = []
        currPath = [0]

        def dfs(currNode):
            if currNode == n - 1:
                solns.append(currPath[:])

            for nei in graph[currNode]:
                currPath.append(nei)
                dfs(nei)
                currPath.pop()

        dfs(0)
        return solns