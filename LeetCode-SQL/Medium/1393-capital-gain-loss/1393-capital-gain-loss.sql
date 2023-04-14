# Write your MySQL query statement below
select stock_name , 
sum(
    case when operation='buy' then price*(-1)
    when operation = 'sell' then price
    else '' end
    ) capital_gain_loss
from Stocks
group by stock_name