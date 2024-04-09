SELECT name AS Employee FROM Employee emp
WHERE salary > (SELECT salary FROM Employee WHERE emp.managerId = id );
