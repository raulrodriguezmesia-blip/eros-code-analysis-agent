CREATE MODEL bqml_tutorial.sales_forecasting_model
OPTIONS(
  MODEL_TYPE = 'ARIMA_PLUS',
  time_series_timestamp_col = 'date_col',
  time_series_data_col = 'total_sales',
  time_series_id_col = 'product_id'
) AS
SELECT
  SUM(sale_price) AS total_sales,
  DATE(created_at) AS date_col,
  product_id
FROM `bigquery-public-data.thelook_ecommerce.order_items` AS t1
INNER JOIN `bigquery-public-data.thelook_ecommerce.products` AS t2
ON t1.product_id = t2.id
GROUP BY date_col, product_id;