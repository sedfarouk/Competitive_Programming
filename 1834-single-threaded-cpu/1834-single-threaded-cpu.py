class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        priorityHeap = []
        ans = []
        timeHeap = []
        
        for i in range(len(tasks)):
            heappush(timeHeap, (tasks[i][0], tasks[i][1], i))
        
        time = timeHeap[0][0]
        while timeHeap:
            if time >= timeHeap[0][0]:
                p = heappop(timeHeap)
                heappush(priorityHeap, (p[1], p[2]))

            else:
                if priorityHeap:
                    q = heappop(priorityHeap)
                    ans.append(q[1])
                    time += q[0]

                else:
                    time = timeHeap[0][0]
            
        while priorityHeap:
            ans.append(heappop(priorityHeap)[1])
            
        return ans

        