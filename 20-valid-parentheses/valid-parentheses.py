class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        brackets = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in brackets:
                if not stk or stk[-1] != brackets[ch]:
                    return False
                stk.pop()
            else:
                stk.append(ch)

        return len(stk) == 0