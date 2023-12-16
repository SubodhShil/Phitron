-- Practice
USE dummydb;

SELECT * FROM countries;

SELECT * FROM DEPARTMENTS;

SELECT * FROM employees;

-- SELECT: show only first and last name from the employees table
SELECT first_name, last_name 
FROM employees;

-- WHERE: show employees with department id 30 to 50
SELECT first_name, department_id
FROM employees
WHERE department_id >= 30 and department_id <= 50
ORDER BY department_id ASC;

-- Arithmetic operation
SELECT FIRST_NAME, SALARY, SALARY + SALARY * 0.05 AS SALARY_WITH_DIWALI_BONUS
FROM employees ;

-- DISTINCT: show all job id (if duplicate show once)
SELECT DISTINCT job_id 
FROM employees;

-- ORDER BY
SELECT * 
FROM EMPLOYEES
ORDER BY SALARY DESC
-- LIMIT
-- LIMIT 4, 10; -- show me from 5th row, next 10 entry or data row 
-- OFFSET: the above limit can be done following way 
LIMIT 9
OFFSET 4;

-- LIKE 
-- '%ee' মানে ee দিয়ে শেষ হবে । 
-- 'ee%' মানে ee দিয়ে শুরু হবে ।
-- '%ee' মানে  word এর মাঝে কোথাও ee থাকতে হবে ।
SELECT * 
FROM Employees 
WHERE last_name LIKE '%ee%';