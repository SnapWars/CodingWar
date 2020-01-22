select max(e1.Salary) as SecondHighestSalary from Employee e1 where e1.Salary < (select max(e2.salary) from Employee e2)
