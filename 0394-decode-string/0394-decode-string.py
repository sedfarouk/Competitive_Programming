class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0

        while i < len(s):
            num = 0
            while s[i].isdigit():
                num *= 10
                num += int(s[i])
                i += 1
            
            if s[i]=='[':
                stack.append(str(num))
            
            elif s[i].isalpha():
                stack.append(s[i])

            else:
                t = ""
                while stack[-1].isalpha():
                    t += stack.pop()
                t *= int(stack.pop())
                stack.append(t)
            i += 1

        ans = ""
        while stack:
            ans += stack.pop()
        return ans[::-1]