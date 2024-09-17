class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        incoming = [0]*n
        increase = [0]*n

        for preq, course in relations:
            graph[preq-1].append(course-1)
            incoming[course-1] += 1

        queue = deque([i for i in range(n) if incoming[i]==0])
        ans = 0
        
        while queue:
            level = len(queue)

            for _ in range(level):
                curr = queue.popleft()
                ans = max(ans, time[curr])

                for nei in graph[curr]:
                    incoming[nei] -= 1
                    increase[nei] = max(increase[nei], time[curr])

                    if incoming[nei]==0:
                        queue.append(nei)
                        time[nei] += increase[nei]
                        
        return ans

