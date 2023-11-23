class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # if edges[0][0] == edges[1][1] or edges[0][0]==edges[1][0]:
        #     return edges[0][0]
        # return edges[0][1]

        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        for key, val in graph.items():
            if len(val)==len(graph.keys())-1:
                return key

        