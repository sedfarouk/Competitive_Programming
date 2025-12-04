class Solution:
    def calculate(self, s: str) -> int:
        opStack, numStack = [], []

        def evalExp(x, y, op):
            if op == '+':
                return x + y
            if op == '-':
                return x - y
            if op == '*':
                return x * y
            if op == '/':
                d = abs(x) // y
                return -d if x < 0 else d  

        bodmas = {'+': ('*', '/', '+'), '*': ('/', '*'), '/': ('/', '*'), '-': ('+', '*', '/')}

        n = len(s)
        curr = 0
        for i in range(n):
            if s[i] == ' ':
                continue

            if s[i].isdigit():
                curr = curr * 10 + (int(s[i]) if curr >= 0 else -int(s[i]))

                if i > 0 and s[i - 1] == '-':
                    curr *= -1

            else:
                numStack.append(curr)
                curr = 0

                while opStack and opStack[-1] in bodmas[s[i]]:
                    num2, num1 = numStack.pop(), numStack.pop()
                    op = opStack.pop()
                    numStack.append(evalExp(num1, num2, op))
                opStack.append(s[i] if s[i] != '-' else '+')

        numStack.append(curr)
        
        while opStack:
            num2, num1 = numStack.pop(), numStack.pop()
            op = opStack.pop()
            numStack.append(evalExp(num1, num2, op))

        return numStack.pop()

                
                    