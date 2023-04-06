select  (select distinct salary from Employee
order by salary desc
limit 1 offset 1) SecondHighestSalary

























































# limit 1 offset 1은 
## limit 1 : 1개 row를 가져오는 것인데,
## offset 1 : 1번 이후의 행 (= 2번 행) 부터 가져오라는 것

# select (select distinct salary   from Employee
# order by salary desc
# limit 1
# offset 1) SecondHighestSalary





















































# 아무 것도 없는 것 select하면 null 생김
# select 
# (select distinct salary from Employee
# order by salary desc
# limit 1 offset 1) SecondHighestSalary



























































# select distinct salary from employee order by salary desc limit 1 offset 1

# # select distinct salary as SecondHighestSalary
# # from Employee
# # order by salary DESC
# # limit 1 offset 1;



# select (select distinct salary 
# from employee
# order by salary desc
# limit 1 offset 1) SecondHighestSalary



# select (
# select distinct salary from Employee
# order by salary desc
# limit 1 offset 1) as SecondHighestSalary


