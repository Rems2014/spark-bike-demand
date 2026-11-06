# Extend the project yourself

Start with a copy of an existing SQL file. Add your query under `sql/` with a new numbered name, then rerun `python src/analyze.py`. Every SQL file must contain one query that returns a table. The available view is `rentals`; inspect its columns in `src/analyze.py`.

1. **Filter:** Show hours with more than 800 rentals. Return date, hour, and rentals. Sort by rentals descending.
2. **Group:** Find average demand by year using `YEAR(rental_date)`.
3. **CASE:** Classify hour into morning (6–11), afternoon (12–17), evening (18–23), and overnight (0–5). Compare average demand and observed counts.
4. **Subquery:** Find hours with rentals above the overall average. Hint: `WHERE rentals > (SELECT AVG(rentals) FROM rentals)`.
5. **Customer mix:** Calculate registered customers' percentage of rentals for each month. Divide summed registered counts by summed total counts; do not average individual percentages.
6. **Window:** Use `ROW_NUMBER()` to identify the busiest hour for each date. Break ties by hour so your result is reproducible.
7. **Join:** Build a weather-code lookup using `VALUES`, join it to rentals, and compare working-day demand within each weather category.
8. **Critical thinking:** Why is a larger average under clear weather insufficient to prove that clear weather caused the increase?

Write three findings in the README, attach the relevant report, and explain one limitation for each finding. Commit that work as your own extension of the starter project.
