SELECT *
FROM ML.FORECAST(MODEL `bqml_tutorial.sales_forecasting_model`,
  STRUCT(
    30 AS horizon,          -- Predict 30 days ahead
    0.95 AS confidence_level -- 95% confidence interval
  )
);