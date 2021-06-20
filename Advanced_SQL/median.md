
### Compute Median
given a table World(name,population), list all the countries at the median in terms of the population

```sql
WITH t AS
    (SELECT *, row_number() OVER (ORDER BY population) rn
    FROM world)

SELECT name
FROM world
WHERE population >
    (SELECT AVG(population) -- get median population
    FROM t
    WHERE rn in
        (SELECT floor((max(rn) + 1) / 2) FROM t 
        UNION 
        SELECT floor((max(rn) + 2) / 2) FROM t))
```

```sql
WITH t AS
    (SELECT name, PRECENTILE_COUNT(0.5) WITHIN GROUP (ORDER BY population) AS median_pop
    FROM world)

SELECT world.name
FROM world JOIN tbl ON world.name = t.name
WHERE world.population > t.median_pop
```
