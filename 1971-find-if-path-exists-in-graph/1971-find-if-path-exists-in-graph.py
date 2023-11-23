class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

            
        def dfs(vertex, visited):
            if vertex==destination:
                return True
            
            visited.add(vertex)
            
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    found = dfs(neighbour, visited)
                    
                    if found:
                        return True
            return False
        
        visited = set()
        
        return dfs(source, visited)

        
        
            
            
        