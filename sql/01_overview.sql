-- One row is an observed hour, not an individual trip.
SELECT MIN(rental_date) AS first_date, MAX(rental_date) AS last_date,
       COUNT(*) AS observed_hours, SUM(rentals) AS total_rentals,
       ROUND(AVG(rentals), 2) AS average_rentals_per_observed_hour,
       ROUND(100.0 * SUM(registered) / SUM(rentals), 2) AS registered_share_percent
FROM rentals
