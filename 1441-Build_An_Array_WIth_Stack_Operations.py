class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []

        stack = deque()
        ptr = 0

        for i in range(1, n+1):
            stack.append(i)
            ans.append("Push")

            if stack[-1] != target[ptr]:
                stack.pop()
                ans.append("Pop")
                ptr -= 1
            
            ptr += 1
            if ptr==len(target):
                return ans
