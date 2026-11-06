# Validation status

Source CSV independently inspected with Python: 17,379 hourly rows, 3,292,679 total rentals. Average demand by hour independently calculated: 17:00 = 461.45, 18:00 = 425.51, 08:00 = 359.01.

Spark 4.2.0 completed all six SQL queries on 2026-11-06 using Java 17. The process returned exit code 0. All six CSV reports and results.json were generated. Data quality results: 17,379 rows, zero invalid rows, and 17,379 distinct date/hour pairs. Source CSV totals and peak hourly averages match an independent Python CSV calculation.

Windows-specific handling keeps Python's temporary connection files inside the project and uses short Windows paths for the batch launcher. The environment emitted nonfatal PowerShell-profile, native Hadoop, pandas compatibility, Spark UI port, getconf, and exit-cleanup warnings; these did not prevent SQL execution or report generation. This project uses no pandas API and does not require a Hadoop installation for its local CSV analysis.

Charts are generated from the saved Spark summaries, not from a separate analysis engine.
