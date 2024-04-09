SELECT DISTINCT num AS ConsecutiveNums
FROM (SELECT num, LAG(num) OVER (ORDER BY id) AS previous, LEAD(num) OVER (ORDER BY id) AS current FROM Logs) prev_next
WHERE num=previous AND previous=current;
