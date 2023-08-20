class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x:x[0])
        max_val = intervals[0][1]
        min_val = intervals[0][0]

        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= max_val:
        #         max_val = max(max_val, intervals[i][1])
        #     else:
        #         ans.append([min_val, max_val])
        #         min_val = intervals[i][0]
        #         max_val = intervals[i][1]

        # ans.append([min_val, max_val])

        for i in intervals:
            if not ans or ans[-1][-1] < i[0]:
                ans.append(i)
            else:
                ans[-1][1] = max(ans[-1][1], i[1])

        return ans

        
