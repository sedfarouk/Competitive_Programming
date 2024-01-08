class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ordering = [0]*numCourses
        graph = defaultdict(list)

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            ordering[pre[0]] += 1

        queue = deque([i for i in range(len(ordering)) if ordering[i]==0])

        while queue:
            q = queue.popleft()

            for nei in graph[q]:
                ordering[nei] -= 1
                
                if ordering[nei] == 0:
                    queue.append(nei)

        for num in ordering:
            if num!=0:
                return False
        return True

        