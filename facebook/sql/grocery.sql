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
    (count(case when is_low_fat_flg = 'Y' and is_recyclable_flg ='Y' then product_id end) * 100) 
        / count(product_id) as perc
from products
