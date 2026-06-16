class Solution:
    def processStr(self, s: str) -> str:
        ans = deque()
        d = True

        for c in s:
            if c == '*': 
                if ans: ans.pop() if d else ans.popleft()
            elif c == '#': ans.extend(ans)
            elif c == '%': d = not d
            else: ans.append(c) if d else ans.appendleft(c)
        
        return "".join(list(ans) if d else list(ans)[::-1])