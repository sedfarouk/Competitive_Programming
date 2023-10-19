class Solution:
    def isValid(self, s: str) -> bool:
        stack_1 = deque([i for i in s])
        stack_2 = deque()

        brackets_map = {")":"(", "}":"{", "]":"["}

        while stack_1:
            ch = stack_1.pop()

            if ch==")" or ch=="}" or ch =="]":
                stack_2.append(ch)
            else:
                if not stack_2:
                    return False

                x = stack_2.pop()

                if brackets_map[x] != ch:
                    return False
            
        if stack_2:
            return False

        return True

 
        