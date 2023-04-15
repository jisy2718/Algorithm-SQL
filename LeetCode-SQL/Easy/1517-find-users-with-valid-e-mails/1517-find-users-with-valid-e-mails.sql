# Write your MySQL query statement below
select * from Users
where
# ^ : 뒤의 문자로 문자열 시작, * 앞의 문자열 0개이상 존재
regexp_like(mail, '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com')