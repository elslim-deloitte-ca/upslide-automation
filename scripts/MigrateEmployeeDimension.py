import os

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
os.chdir("../")


def dropDuplicatesAndSortDataFrame(df, sortBy="email"):
    return df.dropna().drop_duplicates().sort_values([sortBy]).reset_index(drop=True)


# Original
## Read original excel
originalDF = (
    pd.read_excel('data/raw/master.xlsx', sheet_name='User Data')
      .rename(columns={
            'E-mail': 'email',
            'Name': 'name',
            'Team': 'businessLine',
            'Title': 'title',
            'Time saved (over the period)': 'timeSaved',
            'Number of clicks (over the period)': 'numberOfClicks',
            'mm/dd/yy': 'reportingDate',
            'Region': 'region',
            'City': 'city'})
)

originalDF = originalDF[['email', 'name', 'businessLine', 'title', 'region', 'city']]

## Clean original excel values
originalDF = originalDF[originalDF["name"].apply(lambda s: "left firm" not in s.lower())] # Remove rows where employee details are "Left Firm"
originalDF["title"] = originalDF["title"] + " [[LEFT FIRM]]"
originalDF["businessLine"] = originalDF["businessLine"] + " [LEFT FIRM]"
originalDF["subBusinessLine"] = originalDF["businessLine"]
originalDF["region"] = originalDF["region"].apply(lambda row: "Ontario" if row == "Toronto" else row) + " [LEFT FIRM]" # Replace Toronto with Ontario in Region column
originalDF["city"] = originalDF["city"].apply(lambda row: "Toronto - Bay Adelaide East" if row == "Toronto" else row) + " [LEFT FIRM]" # Replace Toronto with Ontario in Region column
originalDF["email"] = originalDF["email"].str.lower()
originalDF["name"] = originalDF["name"].str.title() + " [LEFT FIRM]"
originalDF = dropDuplicatesAndSortDataFrame(originalDF)

# Latest
## Get latest talent data (as of 2022 June 30)
currentDF = (
    pd.read_excel('data/raw/talent/FA Headcount report_RITM2154626.xlsx')
      .rename(columns={
            'Work Email Address': 'email',
            'First Name': 'firstName',
            'Last Name': 'lastName',
            'Employee Status': 'employeeStatus',
            'Business Line': 'businessLine',
            'Business Sub-Line': 'subBusinessLine',
            'Geographic Region': 'region',
            'Office Location': 'city',
            'Career Level': 'title'})
)

## Clean columns
currentDF['name'] = (currentDF['firstName'] + ' ' + currentDF['lastName']).str.title()
currentDF["email"] = currentDF["email"].str.lower()

## Select and reorder columns
cleanedCurrentDF = currentDF[['email', 'name', 'employeeStatus',
                              'businessLine', 'subBusinessLine', 'title',
                              'region', 'city']]


# Combined
## Create list of all employee emails from both sources
employeeDF = dropDuplicatesAndSortDataFrame(pd.concat([originalDF[["email"]], cleanedCurrentDF[["email"]]]))

## Enrich full list with latest talent data
employeeDF = employeeDF.merge(cleanedCurrentDF, on="email", how="outer").dropna(subset=["email"]) # Drop rows where emails are missing

## Update status by replacing blank values from unmatched rows
employeeDF["employeeStatus"] = employeeDF["employeeStatus"].apply(lambda status: "Left Firm" if status is np.NAN else status)

## Update values for missing employees with values from original source
employeeDF.update(originalDF, overwrite=False)

## Write combined data to csv
employeeDF.to_csv("data/report/employees.csv", index=False)

print(originalDF.columns)
print(cleanedCurrentDF.columns)
print(employeeDF.columns)
