class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0]*numCourses
        graph = defaultdict(list)

        for preq in prerequisites:
            in_degree[preq[0]] += 1
            graph[preq[1]].append(preq[0])

        ordering = []
        queue = deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)

        while len(queue) > 0:
            q = queue.pop()
            ordering.append(q)

            for subj in graph[q]:
                in_degree[subj] -= 1

                if in_degree[subj]==0:
                    queue.append(subj)

        if len(ordering) < numCourses:
            return []
        return ordering



        