-- SQL Assignment - 4 Queries

-- 1. Select employee details  of dept number 10 or 30
SELECT * 
FROM Emp 
WHERE DeptNo = 10 OR DeptNo = 30;

-- 2. Write a query to fetch all the dept details with more than 1 Employee.
SSELECT d.* 
FROM Dept d
JOIN Emp e ON d.DeptNo = e.DeptNo
GROUP BY d.DeptNo
HAVING COUNT(e.EmpNo) > 1;

-- 3. Write a query to fetch employee details whose name starts with the letter “S”
SELECT * 
FROM Emp 
WHERE Ename LIKE 'S%';

-- 4. Select Emp Details Whose experience is more than 2 years
SELECT * 
FROM Emp 
WHERE TIMESTAMPDIFF(YEAR, Hire_Date, CURDATE()) > 2;

-- 5. Write a SELECT statement to replace the char “a” with “#” in Employee Name ( Ex:  Sachin as S#chin)
SELECT REPLACE(Ename, 'a', '#') AS ModifiedName, * 
FROM Emp;

-- 6. Write a query to fetch employee name and his/her manager name. 
SELECT e.Ename AS EmployeeName, m.Ename AS ManagerName
FROM Emp e
LEFT JOIN Emp m ON e.Mgr = m.EmpNo;

-- 7. Fetch Dept Name , Total Salry of the Dept
SELECT d.Dname, SUM(e.Sal) AS TotalSalary
FROM Dept d
LEFT JOIN Emp e ON d.DeptNo = e.DeptNo
GROUP BY d.Dname;

-- 8. Write a query to fetch ALL the  employee details along with department name, department location, irrespective of employee existance in the department.
SELECT e.*, d.Dname, d.Loc
FROM Dept d
LEFT JOIN Emp e ON e.DeptNo = d.DeptNo;

-- 9. Write an update statement to increase the employee salary by 10 %
UPDATE Emp 
SET Sal = Sal * 1.1;

-- 10. Write a statement to delete employees belong to Chennai location.
DELETE FROM Emp
WHERE DeptNo IN (SELECT DeptNo FROM Dept WHERE Loc = 'Chennai');

-- 11. Get Employee Name and gross salary (sal + comission) .
SELECT Ename, (Sal + COALESCE(Commission, 0)) AS GrossSalary 
FROM Emp;

-- 12. Increase the data length of the column Ename of Emp table from  100 to 250 using ALTER statement
ALTER TABLE Emp MODIFY COLUMN Ename VARCHAR(250);

-- 13. Write query to get current datetime
SELECT NOW();

-- 14. Write a statement to create STUDENT table, with related 5 columns
CREATE TABLE STUDENT (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100),
    DateOfBirth DATE,
    Major VARCHAR(50),
    GPA DECIMAL(3,2)
);

-- 15.  Write a query to fetch number of employees in who is getting salary more than 10000
SELECT COUNT(*) AS EmployeeCount 
FROM Emp 
WHERE Sal > 10000;

-- 16. Write a query to fetch minimum salary, maximum salary and average salary from emp table.
SELECT 
    MIN(Sal) AS MinimumSalary,
    MAX(Sal) AS MaximumSalary,
    AVG(Sal) AS AverageSalary
FROM Emp;

-- 17. Write a query to fetch number of employees in each location
SELECT d.Loc, COUNT(e.EmpNo) AS EmployeeCount
FROM Dept d
LEFT JOIN Emp e ON d.DeptNo = e.DeptNo
GROUP BY d.Loc;

-- 18. Write a query to display emplyee names in descending order
SELECT Ename 
FROM Emp 
ORDER BY Ename DESC;

-- 19. Write a statement to create a new table(EMP_BKP) from the existing EMP table 
CREATE TABLE EMP_BKP AS SELECT * FROM Emp;

-- 20.  Write a query to fetch first 3 characters from employee name appended with salary.
SELECT CONCAT(LEFT(Ename, 3), Sal) 
FROM Emp;

-- 21. Get the details of the employees whose name starts with S
SELECT * FROM Emp WHERE Ename LIKE 'S%';

-- 22. Get the details of the employees who works in Bangalore location
SELECT e.* 
FROM Emp e
JOIN Dept d ON e.DeptNo = d.DeptNo
WHERE d.Loc = 'Bangalore';

-- 23. Write the query to get the employee details whose name started within  any letter between  A and K
SELECT * 
FROM Emp 
WHERE Ename >= 'A' AND Ename < 'L';

-- 24. Write a query in SQL to display the employees whose manager name is Stefen
SELECT e.* 
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo
WHERE m.Ename = 'Stefen';

-- 25. Write a query in SQL to list the name of the managers who is having maximum number of employees working under him
SELECT m.Ename, COUNT(e.EmpNo) AS EmployeeCount
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo
GROUP BY m.EmpNo, m.Ename
ORDER BY EmployeeCount DESC
LIMIT 1;

-- 26. Write a query to display the employee details, department details and the manager details of the employee who has second highest salary
SELECT e.*, d.*, m.*
FROM Emp e
JOIN Dept d ON e.DeptNo = d.DeptNo
JOIN Emp m ON e.Mgr = m.EmpNo
WHERE e.Sal = (
    SELECT MAX(Sal)
    FROM Emp
    WHERE Sal < (SELECT MAX(Sal) FROM Emp)
);

-- 27. Write a query to list all details of all the managers
SELECT DISTINCT m.*
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo;

-- 28. Write a query to list the details and total experience of all the managers
SELECT DISTINCT m.*, TIMESTAMPDIFF(YEAR, m.Hire_Date, CURDATE()) AS Experience
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo;

-- 29. Write a query to list the employees who is manager and  takes commission less than 1000 and works in Delhi
SELECT DISTINCT m.*
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo
JOIN Dept d ON m.DeptNo = d.DeptNo
WHERE m.Commission < 1000
AND d.Loc = 'Delhi';

-- 30. Write a query to display the details of employees who are senior to Martin 
SELECT e.* 
FROM Emp e
JOIN Emp martin ON martin.Ename = 'Martin'
WHERE e.Hire_Date < martin.Hire_Date;
