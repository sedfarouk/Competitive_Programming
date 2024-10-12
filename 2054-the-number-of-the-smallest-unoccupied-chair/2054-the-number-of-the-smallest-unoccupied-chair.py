class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        order = sorted(range(len(times)), key=lambda x:times[x][0])
        free, taken = list(range(len(times))), []

        for i in order:
            ar, lv = times[i]

            while taken and taken[0][0] <= ar:
                heappush(free, heappop(taken)[1])

            pos = heappop(free)
            
            if i==targetFriend: return pos

            heappush(taken, (lv, pos))