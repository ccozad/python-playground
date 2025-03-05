import pandas as pd

# Put your own CSV file name here
df = pd.read_csv('tshirts.csv')

numeric_columns = df.select_dtypes(include=[int, float])
column_sums = numeric_columns.sum(axis=0)

# Remove the integer cast if you want to deal with floats
column_sums = column_sums.astype(int)
print(column_sums)