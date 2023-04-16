# Write your MySQL query statement below


# select category , count(*) accounts_count 
#     from 
#     (select 
#         (case 
#             when income < 20000 then 'Low Salary'
#             when income between 20000 and 50000 then 'Average Salary'
#             when 50000 < income then 'High Salary'
#             else '' 
#          end) category

#     from Accounts) tmp

# group by category


select 'Low Salary' category, sum(if(income < 20000, 1, 0)) accounts_count  from Accounts
union
select 'Average Salary' category, sum(if(income between 20000 and 50000, 1, 0)) accounts_count  from Accounts
union
select 'High Salary' category, sum(if(income > 50000, 1, 0)) accounts_count  from Accounts