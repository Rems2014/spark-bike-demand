# Dataset attribution

Fanaee-T, H. (2013). **Bike Sharing** [Dataset]. UCI Machine Learning Repository.

- Dataset page: https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset
- DOI: https://doi.org/10.24432/C5W894
- Download: https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip
- License: Creative Commons Attribution 4.0 International, https://creativecommons.org/licenses/by/4.0/
- Downloaded: 2026-11-06.

The original `hour.csv`, `day.csv`, and `Readme.txt` are retained unchanged. The analysis uses only `hour.csv`. Derived summaries rename columns, aggregate hourly observations, and decode weather categories. The raw normalized temperature is retained as normalized temperature; no Celsius conversion is claimed.

`cnt` is the sum of casual and registered rental counts. Each row represents an observed date and hour. `workingday=0` means weekend or holiday. The weather labels in the analysis abbreviate the original definitions; see the source Readme for full descriptions.

The downloaded hourly file has 17,379 data rows. Use the actual file's count rather than relying on a website's summary count.
