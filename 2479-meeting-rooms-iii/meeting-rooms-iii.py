class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        scores = [0] * n
        used, available = [], []
        ans = 0

        for st, end in meetings:
            while used and (st >= used[0][0] or len(used) == n):
                other_end, room = heappop(used)
                heappush(available, (room, other_end))

            if available:
                room, other_end = heappop(available)
                end = max(end, other_end + (end - st))
            else:
                room = len(used)

            scores[room] += 1
            if scores[room] >= scores[ans]:
                ans = room if scores[room] > scores[ans] else min(room, ans)
            heappush(used, (end, room))

        return ans