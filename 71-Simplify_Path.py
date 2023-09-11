class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        MyStack = deque()

        for word in path:
            if word=="" or word==".":
                continue  
            elif word==".." and not MyStack:
                continue
            elif word==".." and MyStack:
                MyStack.pop()
            else:
                MyStack.append(word)
        ans = '/' + '/'.join(MyStack)

        return ans

