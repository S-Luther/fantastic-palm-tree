import pandas as pd

# 1. Load the CSV file into a DataFrame
df = pd.read_csv('list.csv')

# 2. Remove completely identical duplicate rows (keeps the first occurrence)
df_cleaned = df.drop_duplicates()

# 3. Save the unique rows back to a new CSV file
df_cleaned.to_csv('output_cleaned.csv', index=False)