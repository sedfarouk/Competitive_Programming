class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = prev = 0
        for b in bank:
            cnt = b.count('1')   

            if cnt > 0:        
                ans += prev * cnt
                prev = cnt

        return ans 


        