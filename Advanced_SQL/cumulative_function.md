### Use of cumulative functions

given table spend(uid, date, spending), get the up-to-date spending for each user.

```sql

SELECT uid, date, SUM(spending)
OVER (PARTITION BY uid 
	ORDER BY date ASC 
	ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_sum
FROM spend;
```
