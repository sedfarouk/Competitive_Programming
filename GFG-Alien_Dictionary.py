class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        graph = {chr(i+97):[] for i in range(k)}
        in_degree = {chr(i+97):0 for i in range(k)}
        
        for i in range(1, len(alien_dict)):
            for j in range(min(len(alien_dict[i]), len(alien_dict[i-1]))):
                if alien_dict[i-1][j]!=alien_dict[i][j]:
                    graph[alien_dict[i-1][j]].append(alien_dict[i][j])
                    in_degree[alien_dict[i][j]] += 1
                    break

        queue = deque([key for key, val in in_degree.items() if val==0])
        lang = ""

        while queue:
            q = queue.pop()
            lang += q
 
            for nei in graph[q]:
                in_degree[nei] -= 1
                
                if in_degree[nei]==0:
                    queue.append(nei)

        return lang
