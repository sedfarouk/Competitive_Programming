class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = deque()
        ans = 0

        for letter in s:
            if letter == ")" and stack and stack[-1]=="(":
                stack.pop()
            elif letter=="(":
                stack.append(letter)
            else:
                ans+=1
        
        ans += len(stack)
        return ans
            
