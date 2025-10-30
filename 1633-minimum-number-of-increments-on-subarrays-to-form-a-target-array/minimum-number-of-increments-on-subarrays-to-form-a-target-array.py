class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        target = [0] + target[:]

        n = len(target)
        stack = []
        prevSmaller = [-1] * n
        for i in range(n - 1, -1, -1):
            while stack and target[stack[-1]] > target[i]:
                prevSmaller[stack.pop()] = i
            stack.append(i)

        stack = []
        prevGreater = [-1] * n
        for i in range(n - 1, -1, -1):
            while stack and target[stack[-1]] <= target[i]:
                prevGreater[stack.pop()] = i
            stack.append(i)

        ans = 0
        for i in range(1, n):
            if prevSmaller[i] > prevGreater[i]:
                ans += target[i] - target[prevSmaller[i]]

        return ans 

        


            


        