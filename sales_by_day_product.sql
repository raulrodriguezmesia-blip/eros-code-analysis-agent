SELECT 
    DATE(order_items.created_at) AS order_date,
    order_items.product_id,
    products.name AS product_name,
    ROUND(SUM(order_items.sale_price), 2) AS total_sales
FROM 
    `bigquery-public-data.thelook_ecommerce.order_items` AS order_items
LEFT JOIN 
    `bigquery-public-data.thelook_ecommerce.products` AS products
ON 
    order_items.product_id = products.id
GROUP BY 
    order_date,
    order_items.product_id,
    product_name
ORDER BY 
    total_sales DESC;