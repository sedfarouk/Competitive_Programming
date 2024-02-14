class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)

        idx = -1
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                idx = i-1

        if idx==-1: return arr
        
        pos = idx+1
        for i in range(idx+1, n):
            if arr[idx] > arr[i] > arr[pos]:
                pos = i

        arr[pos], arr[idx] = arr[idx], arr[pos]
        return arr
        
                    
            