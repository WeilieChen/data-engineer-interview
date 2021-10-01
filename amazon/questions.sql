select manager_id
from employee
group by manager_id
order by count(emp_id) desc
limit 1


with summary_orders as (
  select
    date_trunc('month', order_date)::date as month_begin_date,
    count(order_id) as total_orders_placed,
    sum(order_amount) as total_order_amount
  from cust_orders
  group by 1
),
summary_accounts as (
  select
    date_trunc('month', account_creation_date)::date as month_begin_date,
    count(cust_id) as total_accounts
  from customers
  group by 1
)
select 
  c.month_begin_date, 
  coalesce(total_accounts, 0), 
  coalesce(total_orders_placed, 0), 
  coalesce(total_order_amount, 0)
from calendar c
left join summary_orders o on o.month_begin_date = c.month_begin_date
left join summary_accounts a on a.month_begin_date = c.month_begin_date

select cust_id
from cust_orders
group by cust_id
having count(order_id) <= 2 or sum(order_amount) <= 100