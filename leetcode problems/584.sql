"""
SQL Schema
Pandas Schema
Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
 

Find the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output: 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
"""

----------------------------------------------------------------------------------------

"""
Variant 1:
-Beats about half of accepted solutions in terms of RT speed.
-Not surprisingly has RT complexity of O(N) where N is the number of rows in the table. 
"""

# Write your MySQL query statement below
SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS NULL

----------------------------------------------------------------------------------------

"""
Variant 2:
-The other solution provided in the LC Editorial section which uses a different symbol
for the 'not equal to' operator.
-Again beats about half of accepted solutions in terms of RT speed. There aren't a lot
of possibilities for this problem.
-Not surprisingly also has RT complexity of O(N) where N is the number of rows in the 
table.
"""

SELECT name FROM customer WHERE referee_id <> 2 OR referee_id IS NULL;


----------------------------------------------------------------------------------------

"""
Variant 3:
-This solution written in Python/Pandas I got help with from ChatGPT ;).
-Not sure if it is means as compared to other Pandas-based solutions, but LC saying it
beats ~88% and 90% of accepted answers in terms of RT and memory efficiency respectively. 
-Analysis tool says O(N) for both time and space complexity, but also says it is O(N) for
the space complexity when we don't use an intermediate dataframe variable filtered_df
and instead return just the original dataframe operated on. I think this is correct 
though, and Python/Pandas needs to make memory for a new dataframe even if we don't use
an intermediate variable.
"""

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Apply the filter
    #filtered_df = customer[(customer['referee_id'] != 2) | (customer['referee_id'].isnull())]

    # Select only the 'name' column
    #result = filtered_df[['name']]
    return customer[(customer['referee_id'] != 2) | (customer['referee_id'].isnull())][['name']]
