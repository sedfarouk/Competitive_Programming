class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currStr = ""
        currNum = 0

        for ch in s:
            if ch == '[':
                stack.append(currStr)
                stack.append(currNum)
                currStr, currNum = "", 0

            elif ch == ']':
                prevNum, prevStr = stack.pop(), stack.pop()
                currStr = prevStr + currStr * prevNum

            elif ch.isdigit():
                currNum = currNum * 10 + int(ch)
            
            else:
                currStr += ch

        return currStr
                
