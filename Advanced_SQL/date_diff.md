### Use Datediff()

given table weather(id,recorddate, temperature), find out dates whose temperature is higher than that of their previous day.

```sql
SELECT w1.id
FROM weather AS w1, weather AS w2
WHERE
    DATEDIFF(w1.recorddate, w2.recorddate) = 1
    AND w1.temperature > w2.temperature
```
