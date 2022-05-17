import os
import pandas as pd
import polars as pl
from pprint import pprint

# import openpyxl
# import pyarrow

os.chdir(r'../')

# Master is taken from the Jan - April extract
pandasDF = pd.read_excel('data/raw/master.xlsx', sheet_name='User Data')
masterDF = pl.DataFrame(pandasDF)

print(masterDF.head())
# pandasDF.head()