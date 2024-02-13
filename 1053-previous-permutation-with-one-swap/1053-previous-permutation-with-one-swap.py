class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        monostack = deque()
        n = len(arr)
        prevGreater = [-1]*n

        for i in range(len(arr)-1, -1, -1):
            while monostack and arr[monostack[-1]] < arr[i]:
                prevGreater[monostack.pop()] = i
            monostack.append(i)

        ans = [0]*n
        for i in range(n-1, -1, -1):
            if prevGreater[i]!=-1:
                temp = arr[:]
                temp[i], temp[prevGreater[i]] = temp[prevGreater[i]], temp[i]
                if temp!=arr:
                    ans = max(temp, ans)
        return ans if ans!=[0]*n else arr
            

