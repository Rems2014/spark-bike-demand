-- JOIN a lookup table to replace codes with readable descriptions.
WITH weather_labels AS (
    SELECT * FROM VALUES
      (1, 'Clear or partly cloudy'), (2, 'Mist or cloudy'),
      (3, 'Light rain or snow'), (4, 'Heavy rain or snow')
    AS labels(code, description)
)
SELECT w.description AS weather, COUNT(*) AS observed_hours,
       ROUND(AVG(r.rentals), 2) AS average_rentals
FROM rentals r JOIN weather_labels w ON r.weather_code = w.code
GROUP BY w.code, w.description ORDER BY w.code
