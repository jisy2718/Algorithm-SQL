select email from Person
group by email
having count(*)>1


















# select email Email from Person
# group by email
# having count(email)>1





























































# # Write your MySQL query statement below
# select email from person
# group by email
# having count(id) >= 2


# SELECT distinct a.Email
# FROM Person a JOIN Person b
# ON (a.Email = b.Email)
# WHERE a.Id <> b.Id