class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        prevSmaller = [-1] * n
        monoStack = deque()
        res = [0] * n

        for i in range(n):
            while monoStack and arr[monoStack[-1]] > arr[i]:
                monoStack.pop()

            if monoStack:
                prevSmaller[i] = monoStack[-1]
            monoStack.append(i)

        for i in range(n):
            j = prevSmaller[i]
            res[i] = res[j] + arr[i]*(i-j)

        return sum(res) % (10**9 + 7)
        
