
### Window Function

given table login(uid, login_date, login_time, ip), get the first login ip by each user on each day

```sql

with t as
(SELECT *, ROW_NUMBER() OVER (PARTITION BY uid, login_date ORDER BY login_time asc) AS rn
FROM login)

SELECT uid, login_date, login_time, ip
FROM t
WHERE rn=1;
```
