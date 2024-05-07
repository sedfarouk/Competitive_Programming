class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        arr = [0]*len(s)

        for i, ch in enumerate(s):
            if ch=="(":
                stack.append((ch, i))
            else:
                if stack and stack[-1][0]=="(":
                    br, idx = stack.pop()
                    arr[idx] = arr[i] = 1       
                else:
                    stack.append((ch, i))

        maxx = curr = 0
        for c in arr:
            if c==1:
                curr += 1
            else:
                maxx = max(maxx, curr)
                curr = 0
        return max(maxx, curr)
            

