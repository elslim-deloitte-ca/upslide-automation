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

practitionerDF = renamedDF[['email', 'name', 'team', 'title', 'region', 'city']].drop_duplicates()

# print(renamedDF.shape)
# print(practitionerDF.shape)

# renamedDF.to_csv('data/processed/usage.csv', index=False)
# practitionerDF.to_csv('data/processed/practitioners.csv', index=False)
