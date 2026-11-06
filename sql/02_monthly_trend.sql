-- GROUP BY aggregates the hourly rows into calendar months.
SELECT DATE_FORMAT(rental_date, 'yyyy-MM') AS month,
       SUM(rentals) AS total_rentals, COUNT(*) AS observed_hours,
       ROUND(AVG(rentals), 2) AS average_hourly_rentals
FROM rentals
GROUP BY DATE_FORMAT(rental_date, 'yyyy-MM')
ORDER BY month
