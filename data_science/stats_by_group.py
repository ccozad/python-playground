# We'll group by a given column and calculate statistics for
# each group
#
# Reference:
# https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58

import pandas as pd

df = pd.DataFrame({
    'Address': ['123 Main Street', '456 Centerline Road', '323 Arden Way', '5000 Smith Lane', '200 Darling Way', '1920 Cesna Blvd'],
    'ZipCode': ['95431', '95630', '95630', '95431', '95630', '95431'],
    'SalePrice': [425000, 376000, 571432, 498321, 387499, 430060]
})

print('\nHere is the data frame we are using')
print(df)

print('\nA data frame can be grouped by one or more columns')
df_groups = df.groupby('ZipCode')
print('Then aggregate functions can be run on a column for each group')
median_by_zip = df_groups ['SalePrice'].median()
average_by_zip = df_groups ['SalePrice'].mean()
min_by_zip = df_groups ['SalePrice'].min()
max_by_zip = df_groups ['SalePrice'].max()

print('\nHere is the median of each zip code')
print(median_by_zip)

print('\nHere is the average of each zip code')
print(average_by_zip)

print('\nHere is the min of each zip code')
print(min_by_zip)

print('\nHere is the max of each zip code')
print(max_by_zip)
