"""
1757. Recyclable and Low Fat Products
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
 

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.
"""

----------------------------------------------------------------------------------------

"""
Variant 1:
My initial stab at writing the SQL query. Beats ~50% of accepted answers in terms of RT 
efficiency
"""

'''Write your MySQL query statement below'''
SELECT product_id
FROM Products
WHERE low_fats = 'Y' and recyclable = 'Y';

----------------------------------------------------------------------------------------

"""
Variant 2:
The official solution given by LC for doing the query in SQL. Should be the exact same
functionally and have the same RT efficiency as the query I wrote. It's just written in
a more conventional style.
""" 

SELECT
    product_id
FROM
    Products
WHERE
    low_fats = 'Y' AND recyclable = 'Y'

"""
I will practice doing the same querying except on a dataframe using pandas. See 1757.py
"""