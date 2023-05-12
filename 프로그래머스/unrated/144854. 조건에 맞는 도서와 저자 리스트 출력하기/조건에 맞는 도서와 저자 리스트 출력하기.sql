-- 코드를 입력하세요
SELECT b.book_id BOOK_ID, a.author_name AUTHOR_NAME,  left(b.published_date,10) PUBLISHED_DATE from book b

inner join author a
on b.author_id = a.author_id
and b.category = '경제'

order by b.published_date asc