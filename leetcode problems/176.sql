"""
176. Second Highest Salary
Solved
Medium
Topics
Companies
SQL Schema
Pandas Schema
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
"""

----------------------------------------------------------------------------------------

"""
Variant 1:
The first valid solution for the SQL problem I was able to arrive at using ChatGPT. This
solution beats ~34% of accepted answers in terms of RT efficiency. 
"""

SELECT 
    CASE 
        WHEN COUNT(DISTINCT salary) < 2 THEN NULL
        ELSE (SELECT DISTINCT salary 
              FROM Employee 
              ORDER BY salary DESC 
              LIMIT 1 OFFSET 1)
    END AS SecondHighestSalary
FROM Employee;

----------------------------------------------------------------------------------------

"""
Variant 2:
The official solution for 'Approach 1: Using sub-query and LIMIT clause' given by LC for 
this SQL problem. This solution utilizes an inner query with the `LIMIT` clause to retrieve 
the second highest distinct salary. To ensure that `NULL` is returned if the number of 
distinct salaries is less than 2, the outer query selects the result of the inner query, 
which is executed as a subquery. If there is no second highest salary, the result will be 
`NULL`. This solution beats ~37% of accepted answers in terms of RT efficiency.
"""

SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;

----------------------------------------------------------------------------------------

"""
Variant 3:
The official solution for 'Approach 2: Using IFNULL and LIMIT clause' given by LC for this 
SQL problem. This solution uses the IFNULL function to return the first argument if it is 
not NULL, otherwise it returns the second argument, 'NULL'. This gives us the correct solution 
of one row containing NULL (if there is no such second highest salary) instead of just an 
empty table. This solution beats ~35% of accepted answers in terms of RT efficiency.
"""

SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
;

----------------------------------------------------------------------------------------

"""
Based on averages of RT efficiency compared to all accepted answers, the above 3 variants
seem to be roughly equal.
"""