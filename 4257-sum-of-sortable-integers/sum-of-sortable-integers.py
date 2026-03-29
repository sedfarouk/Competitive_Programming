MAXX = 10 ** 5
DIVS = [[] for _ in range(MAXX + 1)]
for i in range(1, MAXX + 1):
    for j in range(i, MAXX + 1, i):
        DIVS[j].append(i)

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in DIVS[n]:
            sortable = True
            prevMx = prevMn = 0
            for i in range(0, n - k + 1, k):
                br = 0
                currMx = currMn = nums[i]
                for j in range(i + 1, i + k):
                    if nums[j] < nums[j - 1]:
                        br += 1
                        if br > 1 or nums[i] < max(nums[j:i+k]): 
                            br += 1
                            break

                    currMx = max(currMx, nums[j])
                    currMn = min(currMn, nums[j])
                
                if br > 1 or prevMx > currMx or prevMn > currMn or prevMx > currMn:
                    sortable = False
                    break
                prevMx = currMx; prevMn = currMn
            ans += k if sortable else 0
        
        return ans 
            
            