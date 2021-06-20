
### Application of Window Function

given tables employee(id, name, salary, departmentid) and department(id,name), find out top 3 employee salaries for each department

```sql

WITH e AS
    (SELECT *, DENSE_RANK() OVER (PARTITION BY departmentid
                                 ORDER BY salary DESC) rn
    FROM employee)

SELECT d.name AS department, e.name AS employee, salary
FROM e JOIN department AS d
    ON e.departmentid = d.id AND rn <= 3
```
