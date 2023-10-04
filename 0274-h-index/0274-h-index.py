class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cnt = [0] * (max(citations)+1)

        for citation in citations:
            cnt[citation]+=1

        running_sum = 0
        for i in range(len(cnt)-1,-1,-1):
            running_sum += cnt[i]
            
            if running_sum >= i:
                return i


            
