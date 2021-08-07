/* 
sales (
    product_id
    store_id
    customer_id
    promotion_id
    store_sales
    store_cost
    units_sold
    transaction_date
)

products (
    product_id
    product_class_id
    brand_name
    product_name
    is_low_fat_flg
    is_recyclable_flg
    gross_weight
    net_weight
)

promotions (
    promotion_id
    promotion_name
    media_type
    cost
    start_date
    end_date
)

product_classes (
    product_class_id
    product_subcategory
    product_category
    product_department
    product_family
) 
 */

-- What percent of all products in the grocery chain's catalog are both low fat and recyclable?
select 
    count(case when is_low_fat_flg = 'Y' and is_recyclable_flg ='Y' then product_id end) * 100
        / count(product_id) as perc
from products

-- What are the top five (ranked in decreasing order) single-channel media types that correspond to the 
-- most money the grocery chain had spent on its promotional campaigns?
select media_type
from promotions
group by media_type
order by sum(cost) desc
limit 5

-- Find top 5 sales products having promotions
select product_id
from sales s 
where promotion_id is not null
group by product_id
order by sum(store_cost * units_sold) desc
limit 5

-- What percentage of sales happened on first and last day of the promotion?
select s.product_id,
    sum(case when s.transaction_date = p.start_date then (store_cost * units_sold) end) * 100 / sum((store_cost * units_sold)) as first_perc,
    sum(case when s.transaction_date = p.end_date then (store_cost * units_sold) end) * 100 / sum((store_cost * units_sold)) as last_perc
from sales s
join promotion p on p.promotion_id = s.promotion_id
group by product_id

-- Percent of sales that had a valid promotion, the VP of marketing
-- wants to know what percent of transactions occur on either
-- the very first day or the very last day of a promotion campaign.
select count(case when s.promotion_id > 0 then store_sales end) * 100 / (select count(s.store_sales) FROM sales)
from sales s
join promotion p on p.promotion_id = s.promotion_id
where s.transaction_date = p.start_date and s.transaction_date = p.end_date

-- What brands have an average price above $3 and contain at least 2 different products?
select p.brand_name
from products p 
join sales s on s.product_id = p.product_id
group by p.brand_name
having count(distinct product_id) >= 2
and avg(store_cost) > 3

-- To improve sales, the marketing department runs various types of promotions.
-- The marketing manager would like to analyze the effectiveness of these promotion campaigns.
-- In particular, what percent of our sales transactions had a valid promotion applied?