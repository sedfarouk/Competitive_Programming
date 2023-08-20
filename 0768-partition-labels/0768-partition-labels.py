class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i,c in enumerate(s)}
        start = end = 0
        output = []
        for i,c in enumerate(s):
            end = max(end,last[c])
            if i == end:
                output.append(end-start+1)
                start = i + 1
        return output


        # ans = []
        # hashmap = {}
        # s_reversed = list(reversed(s))
        # s_set = list(set([i for i in s]))

        # for i in s_set:
        #     hashmap[i] = [s.index(i)]

        # for i in s_set:
        #     hashmap[i].append(len(s) - s_reversed.index(i)-1)

        # vals = sorted(hashmap.values(), key=lambda x:x[0])
        
        # max_num = vals[0][1]
        # sub = vals[0][0]
        # for i in range(1, len(vals)):
        #     if vals[i][0] <= max_num:
        #         max_num = max(max_num, vals[i][1])
        #     else:
        #         ans.append(max_num-sub+1)
        #         sub = vals[i][0]
        #         max_num = vals[i][1]
        
        # ans.append(max_num-sub+1)

        # return ans
            
        
        

            
        
        