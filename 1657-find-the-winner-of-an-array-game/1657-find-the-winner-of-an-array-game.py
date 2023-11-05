class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        stack = deque()
        stack.append(arr[0])

        cnt = 0
        for i in range(1, len(arr)):
            if cnt==k:
                return stack[-1]
            if stack[-1] > arr[i]:
                cnt += 1
                continue
            else:
                stack.pop()
                stack.append(arr[i])
                cnt = 1

        return stack[-1]