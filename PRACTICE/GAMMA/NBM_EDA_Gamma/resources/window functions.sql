-- create row number for each state  ordering frequency highest to lowest in 2000
SELECT state, name, frequency, row_number() 
OVER(PARTITION BY state ORDER BY FREQUENCY DESC) as name_order
FROM names
WHERE year = 2000;

-- create ranking for each state  ranking frequency highest to lowest in 2000 (duplicates tie)
-- then pick the 5th ranked names for each state
SELECT * FROM (
SELECT state, name, frequency, rank() 
OVER(PARTITION BY state ORDER BY FREQUENCY DESC) as name_rank
FROM names
WHERE year = 2000)
WHERE name_rank = 5;

-- create percentile rank for frequency of names in California in 2000
SELECT state, name, frequency, percent_rank() 
OVER(PARTITION BY state ORDER BY FREQUENCY) as name_percentile
FROM names
WHERE year = 2000 and state = 'CA' 
ORDER BY name_percentile DESC;

-- subquery to select only names below the 90th percentile
SELECT * FROM (
SELECT state, name, frequency, percent_rank() 
OVER(PARTITION BY state ORDER BY FREQUENCY) as name_percentile
FROM names
WHERE year = 2000 and state = 'CA' 
ORDER BY name_percentile DESC)
WHERE name_percentile < .9

-- Create conditional table aggregating name totals by state
WITH name_totals AS 
(SELECT name, state, sum(frequency) AS total_frequency
FROM names
GROUP BY name, state)

-- Create a ranking of total frequencies for each state (filtering to california to limit output)
SELECT name, state, total_frequency, rank() 
OVER(PARTITION BY state ORDER BY total_frequency DESC) AS name_rank
FROM name_totals
where state = 'CA';

-- aggregate name frequency by state
WITH name_totals AS 
(SELECT name, state, sum(frequency) AS state_frequency
FROM names
GROUP BY name, state)

-- create national frequency from state aggregation table
SELECT name, state, state_frequency,  sum(state_frequency)
OVER(PARTITION BY name ) AS national_frequency
FROM name_totals;



