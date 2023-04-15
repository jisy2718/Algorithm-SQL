# Write your MySQL query statement below
select * from Users
where
# ^ : 뒤의 문자로 문자열 시작, * 앞의 문자열 0개이상 존재
regexp_like(mail, '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com')  #정규표현식에서 .을 문자 그대로 나타내려면 \\ 2개로 이스케이프 문자 이용 필요 (.은 문자1개를 의미)