class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        monostack = deque()
        n = len(arr)
        prevGreater = [-1]*n

        for i in range(len(arr)-1, -1, -1):
            while monostack and arr[monostack[-1]] < arr[i]:
                prevGreater[monostack.pop()] = i
            monostack.append(i)
            
        ans = [-1, -1]
        for i in range(n-1, -1, -1):
            if prevGreater[i] != -1:
                if prevGreater[i]>ans[0] or (prevGreater[i]==ans[0] and arr[ans[1]]==arr[i]): 
                    ans = [prevGreater[i], i]
                
        if ans!=[-1, -1]:
            arr[ans[0]], arr[ans[1]] = arr[ans[1]], arr[ans[0]]
            return arr
        return arr
                    
            