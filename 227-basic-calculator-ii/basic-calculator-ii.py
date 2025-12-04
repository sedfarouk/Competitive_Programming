class Solution:
    def calculate(self, s: str) -> int:
        s += '+'
        stack = []
        curr = 0
        last_op = '+'

        for i in range(len(s)):
            if s[i].isdigit():
                curr = curr * 10 + int(s[i])

            elif s[i] in '+*/-':
                if last_op == '+':
                    stack.append(curr)
                elif last_op == '-':
                    stack.append(-curr)
                elif last_op == '*':
                    stack.append(stack.pop() * curr)
                else:
                    stack.append(int(stack.pop() / curr))
                
                last_op = s[i]
                curr = 0

        return sum(stack)
