"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = 0
        
        graph = defaultdict(tuple)
        
        for emp in employees:
            graph[emp.id] = (emp.importance, emp.subordinates)

        def dfs(idx):
            nonlocal importance
            importance += graph[idx][0]
            
            for sub in graph[idx][1]:
                dfs(sub)
            
        dfs(id)
                
        return importance
        