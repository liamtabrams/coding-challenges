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

"""
Variant 1:
My first successful submission using Pandas/Python to return the desired data in the form of a DataFrame.
This solution beats ~55% and ~72% of accepted answers in terms of RT and memory efficiency respectively.
Since the variable for the return data is the only one we create, there really is no way of further 
improving memory efficiency for this particular solution to this Pandas problem. 
"""

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result = products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'), ['product_id']]
    return result



"""
Variant 2:
The official solution given by LC for solving this problem with Pandas/Python. Note the difference between
this and Variant 1. This does not use the loc method and does not subsample the columns in the same line
as the row subsampling, which in my opinion makes this solution easier to read. This solution beats ~44%
and ~70% of accepted answers in terms of RT and memory efficiency respectively. My hypothesis is this is 
equal to Variant 1 in terms of memory efficiency but slightly inferior to Variant 1 in terms of RT
efficiency based on the averages of the reported efficiency metrics. It's possible they are equally
efficient though. More investigation would be needed to validate this claim. 
"""    

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]

    df = df[['product_id']]
    
    return df