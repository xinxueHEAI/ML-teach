### Advanced Join (Uber, Leetcode 262)

Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03".

The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Trips:
```
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| Id          | int      |
| Client_Id   | int      |
| Driver_Id   | int      |
| City_Id     | int      |
| Status      | enum     |
| Request_at  | date     |     
+-------------+----------+
```
Id is the primary key for this table.
The table holds all taxi trips. Each trip has a unique Id, while Client_Id and Driver_Id are foreign keys to the Users_Id at the Users table.
Status is an ENUM type of (‘completed’, ‘cancelled_by_driver’, ‘cancelled_by_client’).

Users:
```
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| Users_Id    | int      |
| Banned      | enum     |
| Role        | enum     |
+-------------+----------+
```
Users_Id is the primary key for this table.
The table holds all users. Each user has a unique Users_Id, and Role is an ENUM type of (‘client’, ‘driver’, ‘partner’).
Status is an ENUM type of (‘Yes’, ‘No’).

```sql


with m as (
SELECT request_at, IF(status='completed',0,1) cancelled 
FROM trips t JOIN users u 
ON t.client_id = u.users_id AND u.banned='No' 
JOIN users d on t.driver_id=d.users_id AND d.banned='No' AND t.request_at BETWEEN "2013-10-01" AND "2013-10-03")

SELECT request_at day, ROUND(AVG(cancelled),2) `Cancellation Rate` FROM m GROUP BY request_at ORDER BY request_at
```
