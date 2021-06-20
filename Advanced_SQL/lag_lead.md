
### Lags and Lead
list all the numbers that appear at least three times in a row

```sql

SELECT DISTINCT num AS num_consecutive
FROM
    (SELECT LEAD(num) OVER (ORDER BY id) AS le,
            LAG(num) OVER (ORDER BY id) AS la,
            Num
    FROM logs) AS t
WHERE le = la AND le = num
```

```sql

SELECT DISTINCT t1.num AS num_consecutive
FROM logs AS t1, logs AS t2, logs AS t3
WHERE
    t1.num = t2.num AND t2.num = t3.num
    AND t1.id + 1 = t2.id AND t1.id + 2 = t3.id
```
