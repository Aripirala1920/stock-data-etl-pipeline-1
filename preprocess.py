import pandas as pd

df = pd.read_csv("data/student_scores.csv")

# Clean nulls
df.fillna(0, inplace=True)

# Add derived metrics
df['Final Grade'] = df[['Test1', 'Test2', 'Assignment']].mean()
df['Attendance%'] = (df['Days Present'] / df['Total Days']) * 100

# Save cleaned data
df.to_csv("data/student_scores_cleaned.csv", index=False)

print("Preprocessing complete.")
