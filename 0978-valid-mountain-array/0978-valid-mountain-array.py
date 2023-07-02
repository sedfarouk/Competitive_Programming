class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3 or sorted(arr, reverse=True)==arr or sorted(arr)==arr:
            return False
        max_num = max(arr)
        pos_max = arr.index(max_num)
        for i in range(1,len(arr)):
            if i<=pos_max and arr[i]<=arr[i-1]:
                return False
            elif i>pos_max and arr[i]>=arr[i-1]:
                return False
        return True