class Solution:
    def average(self, salary: List[int]) -> float:
        maxSalary, minSalary = max(salary), min(salary)
        salary.remove(maxSalary)
        salary.remove(minSalary)
        return sum(salary)/len(salary)