class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        currStr = ''
        currNum = 0

        for i in range(n):
            if s[i] == '[':
                stack.append(currStr)
                stack.append(currNum)
                currNum = 0
                currStr = ''

            elif s[i].isdigit():
                currNum = (currNum * 10) + int(s[i])

            elif s[i] == ']':
                mult, prevStr = stack.pop(), stack.pop()
                currStr = prevStr + mult * currStr

            else:
                currStr += s[i]

        return currStr

            


        
