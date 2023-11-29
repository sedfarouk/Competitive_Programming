class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = defaultdict(list)
        
        for i in range(len(graph)):
            paths[i] = graph[i]
            
        all_paths = []
            
        def dfs(source, path):
            path.append(source)
                
            if source==len(graph)-1:
                all_paths.append(deepcopy(path))
                return 
            
            for neighbour in paths[source]:
                dfs(neighbour, path)
                path.pop()

        dfs(0, [])
        return all_paths
            
        