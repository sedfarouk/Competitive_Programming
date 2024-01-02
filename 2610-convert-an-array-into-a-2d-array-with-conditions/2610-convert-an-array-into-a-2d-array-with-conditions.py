class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        ans = []
        
        for key, val in count.items():
            cnt = 0
            
            while cnt < val:
                if len(ans) > cnt:
                    ans[cnt].append(key)
                else:
                    ans.append([key])
                cnt += 1
        
        return ans
                
        
        