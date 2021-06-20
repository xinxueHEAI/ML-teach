
### Second Highest Entry

given a table employee(id, salary), obtain the second highest record. If there is no second highest, return null

```sql
WITH t AS
    (SELECT DISTINCT salary, DENSE_RANK() OVER (ORDER BY salary DESC) rn
    FROM employee)

SELECT COALESCE(
    (SELECT salary FROM t WHERE rn=2), NULL) AS SecondHighestSalary
```

```sql
SELECT COALESCE(
    (SELECT DISTINCT salary
    FROM employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary
```
