Overview
As a software engineer, I developed this tool to deepen my proficiency in Python-based data science workflows, specifically focusing on the lifecycle of data: from environment isolation and raw data ingestion to cleaning, aggregation, and visualization. This project allowed me to practice defensive programming by identifying and mitigating data formatting risks before they caused system failures.


The dataset used for this analysis is the Nike Sales Dataset, which contains retail transaction records including invoice dates, product categories, and regional sales figures.
Data Source: Nike Sales Dataset on Kaggle
My purpose in writing this software was to build an automated pipeline that can transform "messy" retail data into actionable business intelligence. Specifically, I wanted to determine which product lines drive the most value and whether time-based consumer patterns exist within the sales cycle.

[Software Demo Video
](https://youtu.be/qTPfbhKW3bw)

Data Analysis Results
Question 1: Which product category generates the highest total revenue?
Answer: Men's Street Footwear is the highest revenue generator, totaling $1,999,192.00. It is followed by Women's Apparel and Men's Athletic Footwear.
Question 2: Is there a statistically significant correlation between the time of day and the volume of sales?
Answer: The correlation returned NaN (Not a Number). Upon investigation, the dataset provided only dates with a default time of 00:00. This taught me that while the software is prepared to calculate correlation, the specific data source lacks the granular timestamps necessary for a time-of-day statistical analysis.
Development Environment
IDE: Visual Studio Code.
Environment Management: Python Virtual Environments (venv) were used to isolate dependencies and prevent library version conflicts.
Language: Python 3.9.
Libraries: * Pandas: Used for data manipulation, handling date-time conversions, and performing group-by aggregations.

Matplotlib: Used for the stretch challenge to generate bar charts of the revenue distribution.

Useful Websites
Pandas Documentation - to_datetime
Matplotlib Pyplot Tutorial
Kaggle - Nike Sales Data
Future Work
Implement Multi-Source Merging: Add the ability to join the Nike sales data with inventory datasets to calculate profit margins rather than just gross revenue.
Refine Time Analysis: Incorporate a dataset with precise timestamps to successfully map hourly sales peaks.
Advanced Error Handling: Create a logging system that records specific "dirty data" rows (like the date format error encountered) to a separate file for manual review# module4
# module4
