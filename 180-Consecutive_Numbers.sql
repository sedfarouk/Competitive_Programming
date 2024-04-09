SELECT DISTINCT a.num AS ConsecutiveNums
FROM Logs a, Logs b, Logs c
WHERE a.Id = b.Id - 1 AND b.Id = c.Id - 1 AND a.num = b.num AND b.num = c.num
