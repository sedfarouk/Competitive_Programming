class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        
        for letter in s:
            if stack and stack[-1][0] == letter:
                stack[-1][1] += 1

            else:
                stack.append([letter, 1])

            if stack[-1][1] == k:
                stack.pop()

        return "".join([pair[0]*pair[1] for pair in stack]) 
            
            