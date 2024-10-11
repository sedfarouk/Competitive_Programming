class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        opening  = {times[i][0]:i for i in range(len(times))}
        closing = defaultdict(list)
        assign = {}
        heap = [i for i in range(10**5 + 1)]
        
        for i in range(len(times)):
            closing[times[i][1]].append(i)
        
        for i in range(10**5 + 1):
            while closing[i]:
                heappush(heap, assign[closing[i].pop()])
            
            if i in opening:
                assign[opening[i]] = heappop(heap)
        
        return assign[targetFriend]