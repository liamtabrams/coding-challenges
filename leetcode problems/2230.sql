"""
2230. The Users That Are Eligible for Discount
Solved
Easy

Topics

Companies
SQL Schema
Pandas Schema
Table: Purchases

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| user_id     | int      |
| time_stamp  | datetime |
| amount      | int      |
+-------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
Each row contains information about the purchase time and the amount paid for the user with ID user_id.
 

A user is eligible for a discount if they had a purchase in the inclusive interval of time [startDate, endDate] with at least minAmount amount. To convert the dates to times, both dates should be considered as the start of the day (i.e., endDate = 2022-03-05 should be considered as the time 2022-03-05 00:00:00).

Write a solution to report the IDs of the users that are eligible for a discount.

Return the result table ordered by user_id.

The result format is in the following example.

 

Example 1:

Input:
Purchases table:
+---------+---------------------+--------+
| user_id | time_stamp          | amount |
+---------+---------------------+--------+
| 1       | 2022-04-20 09:03:00 | 4416   |
| 2       | 2022-03-19 19:24:02 | 678    |
| 3       | 2022-03-18 12:03:09 | 4523   |
| 3       | 2022-03-30 09:43:42 | 626    |
+---------+---------------------+--------+
startDate = 2022-03-08, endDate = 2022-03-20, minAmount = 1000
Output:
+---------+
| user_id |
+---------+
| 3       |
+---------+
Explanation:
Out of the three users, only User 3 is eligible for a discount.
 - User 1 had one purchase with at least minAmount amount, but not within the time interval.
 - User 2 had one purchase within the time interval, but with less than minAmount amount.
 - User 3 is the only user who had a purchase that satisfies both conditions.
"""


"""
Variant 1:
My reproduction of Debashish's solution from the Solutions section for this problem. This
solution beats ~50% of accepted answers in terms of RT. According to LC's analysis tool
this solution has time complexity of O(NLogN), where I am guessing that N is the number of
rows in the table 'Purchases'.
"""
CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
	SELECT DISTINCT user_id FROM Purchases WHERE startDate <= time_stamp AND endDate >= time_stamp AND amount >= minAmount ORDER BY user_id;
	
END



"""
Variant 2:
Direct copy of weekwith's solution taken from the Solutions section. This solution is
notable as it uses built-in MySQL functions DATE and DATE_SUB to evaluate and shift
dates even though that is technically not needed, as shown in Variant 1. Still, the
solution summary is good to read as it explains how these functions are the correct
way to cleanly evaluate dates and to stay away from + and - operators. Go to
https://leetcode.com/problems/the-users-that-are-eligible-for-discount/solutions/1975202/be-careful-to-operate-the-date-field-with-or-operation/   .
This solution also beats ~50% of accepted answers in terms of RT. Interestingly enough,
LC's analysis tool reports that the time complexity for this solution is O(N) rather
than O(NLogN) like it does for Variant 1, but I don't understand how that can be the
case. O(NLogN) seems more likely especially because the output needs to be sorted.  
"""
CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
	# Write your MySQL query statement below.
    SELECT DISTINCT user_id AS user_id
    FROM Purchases
    WHERE (
        DATE(time_stamp) BETWEEN startDate AND DATE_SUB(endDate, INTERVAL 1 DAY)
        AND
        amount >= minAmount
    )
    ORDER BY user_id;
END