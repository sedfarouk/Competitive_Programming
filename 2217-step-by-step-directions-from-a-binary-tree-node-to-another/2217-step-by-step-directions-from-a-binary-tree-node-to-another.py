# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, val, ans):
            nonlocal p
            if node.val==val:
                p.append(ans[:])
                return
            
            if not node.left and not node.right:
                return None

            res = None
            if node.left:
                ans.append("L")
                res = res or dfs(node.left, val, ans)
                ans.pop()
            if node.right:
                ans.append("R")
                res = res or dfs(node.right, val, ans)
                ans.pop()
            return res 
        
        p = []
        dfs(root, startValue, [])
        dfs(root, destValue, [])
        pathStart = p[0][:]
        pathDest = p[1][:]

        if pathStart==None:
            return pathDest

        j = 0
        for i in range(min(len(pathStart), len(pathDest))):
            if pathStart[i]!=pathDest[i]:
                break
            j += 1
        pathDest = pathDest[j:]
        pathStart = pathStart[j:]

        return "U"*len(pathStart) + "".join(pathDest)

        
        