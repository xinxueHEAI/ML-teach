### Self Join tables

given employee(id, name, salary, managerid), list the employees who earn more than their managers
```sql

SELECT e.name AS employee
FROM employee AS e JOIN employee AS m
    ON e.managerid = m.id AND e.salary > m.salary
```
