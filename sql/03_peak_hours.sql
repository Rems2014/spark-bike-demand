-- Rank by average demand rather than totals with unequal observation counts.
SELECT hour, COUNT(*) AS observed_hours,
       ROUND(AVG(rentals), 2) AS average_rentals
FROM rentals GROUP BY hour
ORDER BY average_rentals DESC, hour
