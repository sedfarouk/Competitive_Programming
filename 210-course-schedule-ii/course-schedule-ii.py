class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        prereqs = [0] * n

        for course, pre in prerequisites:
            graph[pre].append(course)
            prereqs[course] += 1

        queue = deque([i for i in range(n) if not prereqs[i]])

        ordering = []
        while queue:
            pre = queue.popleft()

            for nei in graph[pre]:
                prereqs[nei] -= 1

                if not prereqs[nei]:
                    queue.append(nei)

            if not prereqs[pre]:
                ordering.append(pre)
            
        return ordering if len(ordering) == n else []