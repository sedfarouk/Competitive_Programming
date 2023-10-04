class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_cnt = Counter(s)
        ans = []
        for i in order:
            if i in s_cnt.keys() and s_cnt[i] > 0:
                ans.append(i*s_cnt[i])
                s_cnt[i] = 0
        
        for key in s_cnt.keys():
            if s_cnt[key]> 0:
                ans.append(key*s_cnt[key])
        return "".join(ans)





