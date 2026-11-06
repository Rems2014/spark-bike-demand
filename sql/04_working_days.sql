-- workingday=0 includes both weekends and holidays.
SELECT CASE WHEN workingday = 1 THEN 'Working day'
            ELSE 'Weekend or holiday' END AS day_type,
       hour, COUNT(*) AS observed_hours,
       ROUND(AVG(rentals), 2) AS average_rentals
FROM rentals GROUP BY workingday, hour
ORDER BY day_type, hour
