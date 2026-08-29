SELECT 
    u.id AS user_id, 
    u.first_name, 
    u.last_name, 
    AVG(oi.sale_price) AS avg_sale_price
FROM 
    `bigquery-public-data.thelook_ecommerce.users` AS u
JOIN 
    `bigquery-public-data.thelook_ecommerce.order_items` AS oi
ON 
    u.id = oi.user_id
GROUP BY 
    u.id, u.first_name, u.last_name
ORDER BY 
    avg_sale_price DESC
LIMIT 10;