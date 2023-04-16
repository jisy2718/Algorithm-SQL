# Write your MySQL query statement below
select e1.employee_id, e1.name, count(e2.employee_id) reports_count  , round(avg(e2.age),0) average_age from Employees e1
left join Employees e2
on e1.employee_id = e2.reports_to   # e1.employee_id가 보고 받는 사람, e2.employee_id가 보고 하는 사람
where e2.reports_to is not null
group by e1.employee_id

order by e1.employee_id


# select * from Employees e1
# left join Employees e2
# on e1.employee_id = e2.reports_to