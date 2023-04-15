# Write your MySQL query statement below

select machine_id, 

round( 
        (
            sum(if(activity_type ='start', timestamp*(-1), 0)) 
            + sum(if(activity_type ='end', timestamp, 0))
        )/count(distinct process_id) 
,3)   processing_time  from Activity

group by machine_id





































# select machine_id, round(avg(each_processing_time),3) processing_time 

# from
#     (
#     # 각 (machine_id, process_id) 페어별로 걸린 시간 측정
#     select machine_id, process_id, sum(if(activity_type ='start', timestamp*(-1), timestamp))     each_processing_time from Activity

#     group by machine_id, process_id
#     ) tmp

# group by machine_id
