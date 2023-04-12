# Write your MySQL query statement below
select s.student_id, s.student_name, s.subject_name , IFNULL(e.attended_exams,0) attended_exams  
from (SELECT * FROM Students CROSS JOIN Subjects ) s  # Student와 Subject table 각 행을 모든 경우 결합


left join 
# Examinations table에서 학생마다 시험치른 횟수 count
(select student_id, subject_name, count(*) attended_exams from Examinations group by student_id, subject_name) e
on s.student_id = e.student_id
and s.subject_name = e.subject_name


order by s.student_id, s.subject_name