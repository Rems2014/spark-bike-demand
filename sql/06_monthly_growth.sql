-- LAG returns the previous month, allowing month-over-month comparison.
WITH monthly AS (
    SELECT DATE_FORMAT(rental_date, 'yyyy-MM') AS month,
           SUM(rentals) AS total_rentals
    FROM rentals GROUP BY DATE_FORMAT(rental_date, 'yyyy-MM')
), previous AS (
    SELECT *, LAG(total_rentals) OVER (ORDER BY month) AS previous_month_rentals
    FROM monthly
)
SELECT *, ROUND(100.0 * (total_rentals - previous_month_rentals)
                 / NULLIF(previous_month_rentals, 0), 2) AS growth_percent
FROM previous ORDER BY month
