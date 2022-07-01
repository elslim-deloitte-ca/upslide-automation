import os
import pandas as pd
pd.set_option('display.max_columns', None)
os.chdir(r'../')

# Talent
rawTalentDF = pd.read_excel('data/raw/talent/FA Headcount report_RITM2154626.xlsx')

## Rename columns
processedTalentDF = rawTalentDF.rename(columns={
    'Work Email Address': 'email',
    'First Name': 'firstName',
    'Last Name': 'lastName',
    'Employee Status': 'employeeStatus',
    'Business Line': 'businessLine',
    'Business Sub-Line': 'subBusinessLine',
    'Geographic Region': 'region',
    'Office Location': 'city',
    'Career Level': 'title'
})

## Combine name columns
processedTalentDF['name'] = processedTalentDF['firstName'] + ' ' + processedTalentDF['lastName']

## Select and reorder columns
processedTalentDF = processedTalentDF[['email', 'name', 'employeeStatus',
                                       'businessLine', 'subBusinessLine', 'title',
                                       'region', 'city']]


# Usage (Master is taken from the Jan - April extract)
rawUsageDF = pd.read_excel('data/raw/master.xlsx', sheet_name='User Data')

## Rename columns
renamedUsageDF = rawUsageDF.rename(columns={
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

## Select usage columns to keep
renamedUsageDF['hasLeft'] = renamedUsageDF['name'].apply(lambda row: True if row == '[Left firm]' else False)
selectUsageDF = renamedUsageDF[['email', 'hasLeft', 'reportingDate', 'timeSaved', 'numberOfClicks']]

# Join usage to talent data
joinedUsageDF = selectUsageDF.merge(processedTalentDF, how='left', on=['email'])

# Clean joined data
joinedUsageDF['status'] = joinedUsageDF.apply(lambda row:
                                                    'Left Firm - Manually Identified' if row['hasLeft'] else ( # Return value if hasLeft is True
                                                    'Left Firm - Talent Data' if pd.isnull(row['employeeStatus']) else # Return value if employeeStatus is null (did not join)
                                                    row['employeeStatus']), axis=1) # Return employeeStatus as default value

joinedUsageDF = joinedUsageDF.fillna('User Data Not Found')

# Select final columns for migration dataframe
migrationDF = joinedUsageDF[['reportingDate', 'email',
                              'name', 'employeeStatus',
                             'businessLine', 'subBusinessLine', 'title',
                             'region', 'city', 'status',
                             'timeSaved', 'numberOfClicks']]


migrationDF.to_csv('data/report/upslide-report.csv', index=False)
print(migrationDF)
print(migrationDF.columns)