## 1. SQL팁

1. [column의 min, max 값으로 column 나누기](https://stackoverflow.com/questions/55438720/how-to-divide-each-row-of-column-by-its-max-min-value-sql)
    + `select col1/(max(col1) over ()) from table`

2. [row to column](https://stackoverflow.com/questions/1241178/mysql-rows-to-columns)

3. [union과 order by 함께쓰는 방법](https://stackoverflow.com/questions/3531251/using-union-and-order-by-clause-in-mysql)

4. [null 값 0으로 변환하기](https://leetcode.com/problems/employee-bonus/discuss/425697/MySQL-solution-(LEFT-JOIN))
    + `SELECT col1, COALESCE(col1, 0) FROM table_a;` : col1의 null 값이 0으로 치환되어 select 됨

5. [column 2개를 1개 column으로 만들 때는 `UNION ALL` 이용](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/discuss/103812/Share-My-Accepted-SQL-Query-using-%22union-all%22-the-first-Accepted-answer-of-all) 



## 2. 과거문제풀이
과거에 풀었던 문제들은 아래에서 찾아볼 수 있습니다.
+ [Leetcode 과거1](https://github.com/jisy2718/TIL/blob/master/SQL/leetcode.md), [Leetcode 과거2](https://github.com/jisy2718/leetcode#readme)