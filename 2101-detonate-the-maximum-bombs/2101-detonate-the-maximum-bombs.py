class Solution:
    def maximumDetonation(self, b: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(b)):
            for j in range(len(b)):
                dist = (b[i][0]-b[j][0])**2 + (b[i][1]-b[j][1])**2
                r = b[i][2]**2

                if i!=j and dist <= r:
                    graph[i].append(j)
        
        def dfs(bomb, visited):
            ans = 1            
            visited.add(bomb)

            for child_bomb in graph[bomb]:
                if child_bomb not in visited:
                    ans += dfs(child_bomb, visited)
            return ans

        maxx = 0
        for i in range(len(b)):
            maxx = max(maxx, dfs(i, set()))
        return maxx