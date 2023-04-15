## 1. SQL팁

1. [column의 min, max 값으로 column 나누기](https://stackoverflow.com/questions/55438720/how-to-divide-each-row-of-column-by-its-max-min-value-sql)
    + `select col1/(max(col1) over ()) from table`

2. [row to column](https://stackoverflow.com/questions/1241178/mysql-rows-to-columns)

3. [union과 order by 함께쓰는 방법](https://stackoverflow.com/questions/3531251/using-union-and-order-by-clause-in-mysql)

4. [null 값 0으로 변환하기](https://leetcode.com/problems/employee-bonus/discuss/425697/MySQL-solution-(LEFT-JOIN))
    + `SELECT col1, COALESCE(col1, 0) FROM table_a;` : col1의 null 값이 0으로 치환되어 select 됨

5. [column 2개를 1개 column으로 만들 때는 `UNION ALL` 이용](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/discuss/103812/Share-My-Accepted-SQL-Query-using-%22union-all%22-the-first-Accepted-answer-of-all) 

6. [column의 누적합 구하기 - 1204번](https://leetcode.com/problems/last-person-to-fit-in-the-bus/discuss/389961/MySQL-beat-100-lol.-Of-course-since-I'm-the-first-one-to-do-this-problem.)

7. [2개 table의 모든 행을 join하기 : Cross join - 1280번](https://leetcode.com/problems/students-and-examinations/submissions/) : cross join 은 table 1이 3개 행, table 2가 4개 행을 가진다면, `select * from table1 cross join table2` 하면 3x4 = 12 개의 행을 가진 table 생성됨

8. [A컬럼 기준 7일 moving average of B컬럼](https://github.com/jisy2718/Algorithm-SQL/tree/master/LeetCode-SQL/Medium/1321-restaurant-growth)

9. [날짜추출법들 : left, extract, month, year](https://leetcode.com/problems/list-the-products-ordered-in-a-period/discuss/497520/Myql-Using-Month-and-Year-function) : `extract`가 가장 빠른듯.
    ```sql
    # yyyy-mm-dd 꼴에서 2020년 2월 추출하고 싶다면
    where order_date like '2020-02%'
    where month(order_date) = 2 and year(order_date) = '2020'
    where left(order_date, 7) = "2020-02"
    where extract(year_month from o.order_date) = 202002
    ```

10. [정규표현식](https://github.com/jisy2718/code_sample/blob/master/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D.ipynb)

## 2. 과거문제풀이
과거에 풀었던 문제들은 아래에서 찾아볼 수 있습니다.
+ [Leetcode 과거1](https://github.com/jisy2718/TIL/blob/master/SQL/leetcode.md), [Leetcode 과거2](https://github.com/jisy2718/leetcode#readme)
