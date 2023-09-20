class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        
        while tokens != []:
            val = tokens.pop(0)
            
            if val=="+" or val=="-" or val=="*" or val=="/":
                val_2 = stack.pop()
                val_1 = stack.pop()
                if val=="+":
                    stack.append(val_1 + val_2)
                elif val=="-":
                    stack.append(val_1 - val_2)
                elif val=="*":
                    stack.append(val_1 * val_2)
                else:
                    stack.append((int(val_1 / val_2)))
            else:
                stack.append(int(val))
        return int(stack[-1])
            
        