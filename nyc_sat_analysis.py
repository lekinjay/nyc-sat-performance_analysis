# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# 1. Which NYC schools have th best math results?
#Filter for schools where average math score is >= 80% of 800 (640)
best_score = schools[schools["average_math"] >= 640]
# select target columns using integer location indexing and sort in descending order
best_math_schools = best_score.iloc[:,[0,3]].sort_values("average_math",ascending=False)
best_math_schools

# 2. What are the top 10 performing schools based on the combined SAT scores?
# creating total SAT score Addition of average_math and average_reading and average_writing
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
# top 10 schools
top_10_schools = schools[["school_name","total_SAT"]].sort_values("total_SAT",ascending=False).head(10)
top_10_schools

# 3. Which single borough has the largest standard deviation in the combined SAT score?
largest_std_dev_mean = schools.groupby("borough")["total_SAT"].agg(["count","mean","std"])
largest_std_dev_mean = largest_std_dev_mean.rename(columns={"count":"num_schools","mean":"average_SAT","std":"std_SAT"})
largest_std_dev = largest_std_dev_mean.reset_index().sort_values("std_SAT",ascending=False).head(1).round(2)
largest_std_dev
