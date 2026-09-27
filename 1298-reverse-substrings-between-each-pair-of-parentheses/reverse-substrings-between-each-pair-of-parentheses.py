class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []

        for ch in s:
            if ch != ')':
                st.append(ch)
            else:
                curr = []
                while st and st[-1] != '(':
                    curr.append(st.pop()[::-1])
                st.pop()
                st.append("".join(curr))
        
        return "".join(st)

