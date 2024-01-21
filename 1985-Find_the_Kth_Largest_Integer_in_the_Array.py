from functools import cmp_to_key

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # heap = [-num for num in nums]
        # heapify(heap)
        # kth = 0
        
        # for _ in range(k):
        #     kth = heappop(heap)
        # return str(-kth)
            
        # Above method won't work in some languages due to integer overflow (len(nums[i]) <= 100). 
        # Best way for interview using cmp_to_key in python
        def sort_func(a, b):
            if len(a) > len(b):
                return -1
            elif len(a) < len(b):
                return 1
            else:
                for a_ch, b_ch in zip(a, b):
                    if a_ch > b_ch:
                        return -1
                    if a_ch < b_ch:
                        return 1
                return 0

        key = cmp_to_key(sort_func)
        nums.sort(key=key)
        return nums[k-1]
                

            

        
        
        
