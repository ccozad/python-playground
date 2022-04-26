# It's simple to load
#
# Reference:
# https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58

import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("price_data.csv")

    print('\nHere is the data frame we loaded from a csv file')
    print(df)
