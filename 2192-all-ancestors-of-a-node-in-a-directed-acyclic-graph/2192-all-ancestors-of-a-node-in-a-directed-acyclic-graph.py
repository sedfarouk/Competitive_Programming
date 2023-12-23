class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degrees = [0]*n
        
        for i in range(len(edges)):
            in_degrees[edges[i][1]] += 1
            graph[edges[i][0]].append(edges[i][1])
            
        ans = [set() for _ in range(n)]
        queue = deque([i for i in range(n) if in_degrees[i]==0])

        while queue:
            q = queue.popleft()
            
            for nei in graph[q]:
                for i in ans[q]:
                    ans[nei].add(i)
                ans[nei].add(q)
                in_degrees[nei] -= 1
                
                if in_degrees[nei]==0:
                    queue.append(nei)
                    
        for i in range(len(ans)):
            ans[i] = list(ans[i])
            ans[i].sort()
        return ans
        