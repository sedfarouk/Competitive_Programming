class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0

        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[k]==0:
                    return ans
                if tickets[i] > 0:
                    tickets[i]-=1
                    ans+=1
        return ans





        