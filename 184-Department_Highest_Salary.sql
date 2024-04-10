SELECT dept.name AS Department, emp.name AS Employee, emp.salary AS Salary
FROM Employee AS emp
LEFT JOIN Department AS dept ON emp.departmentId=dept.id
WHERE (dept.Id, emp.Salary) IN (SELECT departmentId, MAX(salary) 
                                            FROM Employee
                                            GROUP BY departmentId);
