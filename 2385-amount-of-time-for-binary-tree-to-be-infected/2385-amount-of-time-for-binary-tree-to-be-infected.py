# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        
        queue = deque([root])
        while queue:
            q = queue.popleft()
            if q not in graph:
                graph[q] = []
            
            if q.left:
                graph[q].append(q.left)
                graph[q.left].append(q)
                queue.append(q.left)
            if q.right:
                graph[q].append(q.right)
                graph[q.right].append(q)
                queue.append(q.right)
                
        visited = set()
        ans = -1
        queue = deque([num for num in graph.keys() if num.val==start])
        while queue:
            level = len(queue)
            
            if level > 0:
                ans += 1
            
            for _ in range(level):
                q = queue.popleft()
                visited.add(q)
                
                for nei in graph[q]:
                    if nei not in visited:
                        queue.append(nei)        
            
        return ans
        
        