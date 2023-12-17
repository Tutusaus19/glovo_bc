SELECT
    user_id,
    NULLIF(SPLIT_PART(last_5_store_id, '|', 3), '') AS last_store_id_1,
    NULLIF(SPLIT_PART(last_5_store_id, '|', 4), '') AS last_store_id_2,
    NULLIF(SPLIT_PART(last_5_store_id, '|', 5), '') AS last_store_id_3
FROM
    user_data
WHERE
    user_country_code = 'ES'
    AND preferred_city_code != 'BCN'
    AND last_qc_order_date >= CURRENT_DATE - INTERVAL '180 days'
    AND total_groceries_orders > 2;