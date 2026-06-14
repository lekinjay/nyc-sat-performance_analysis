# NYC Public School SAT Performance Analysis
![NYC School Bus](nyc_bus.jpg)

## 📊 Project Overview
This project analyzes the scholastic performance of New York City public high schools using standardized SAT testing data. The analysis investigates performance across distinct core domains (Mathematics, Reading, and Writing) and evaluates geographic variability in test scores across the five boroughs of NYC.

The study answers three core analytical questions:
1. Identifying high-performing institutions in Mathematics.
2. Ranking top overall institutions based on cumulative, engineered compound SAT scores.
3. Identifying regional score variability (standard deviation) across school districts grouped by borough.

## 🛠️ Tech Stack & Methods
- *Language:* Python
- *Libraries:* Pandas, NumPy
- *Key Techniques:* Boolean data subsetting, multi-column feature engineering, positional data slicing (.iloc), index restructuring, and advanced group aggregation (.groupby() paired with .agg()).

## 📈 Key Findings

### 🧮 1. Elite Math Performance
Schools were classified as elite math performers if their average math evaluation score met or exceeded *80% of the maximum possible score (640 out of 800)*. 
- Top performing institutions include *Stuyvesant High School, **Bronx High School of Science, and **Staten Island Technical High School*.

### 🏆 2. Top Cumulative SAT Scores
By engineering a cumulative column (total_SAT) reflecting the combined performance across Reading, Math, and Writing, the top 10 highest-performing schools were isolated. 
- *Stuyvesant High School* leads New York City with a massive combined average SAT score of *2144*.

### 🏙️ 3. Geographic Score Variability
Grouping the schools regionally revealed that *Manhattan* exhibits the highest performance volatility. While it houses some of the most elite schools in the nation, it also displays the largest internal performance disparity:
- *Borough with Largest Disparity:* Manhattan
- *Total Schools Analyzed:* 89
- *Average Combined SAT Score:* 1340.13
- *Standard Deviation (std_SAT):* 230.29
