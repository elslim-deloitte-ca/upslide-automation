import os
import pandas as pd

os.chdir(r'../')

# Master is taken from the Jan - April extract
pandasDF = pd.read_excel('data/raw/master.xlsx', sheet_name='User Data')

renamedDF = pandasDF.rename(columns={
    'E-mail': 'email',
    'Name': 'name',
    'Team': 'team',
    'Title': 'title',
    'Time saved (over the period)': 'timeSaved',
    'Number of clicks (over the period)': 'numberOfClicks',
    'mm/dd/yy': 'reportingDate',
    'Region': 'region',
    'City': 'city'
})

renamedDF.to_csv('data/processed/usage.csv', index=False)
