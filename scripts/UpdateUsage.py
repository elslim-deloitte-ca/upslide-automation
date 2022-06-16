import os
import pandas as pd
pd.set_option('display.max_columns', None)
os.chdir("../")


def update_report_csv(usageFileName, talentFileName, currentReportName, reportingDate):
    # Read raw usage data
    updateDF = pd.read_excel(f"data/raw/usage/{usageFileName}", skiprows=4)

    # Rename columns
    updateDF = updateDF.rename(columns={
        'Mail': 'email',
        'Name': 'name',
        'Team': 'team',
        'Title': 'title',
        'Time Saved (over the period)': 'timeSaved',
        'Number of Clicks (over the period)': 'numberOfClicks',
    })

    # Drop empty and unused columns
    unnamedColumns = [c for c in updateDF.columns if 'Unnamed' in c]
    for unnamedColumn in unnamedColumns:
        updateDF = updateDF.drop(columns=unnamedColumn)

    updateDF = updateDF[['email', 'timeSaved', 'numberOfClicks']]

    # Join talent data
    talentDF = pd.read_excel(f"data/raw/talent/{talentFileName}").rename(columns={'Work Email Address': 'email',
                                                                                    'First Name': 'firstName',
                                                                                    'Last Name': 'lastName',
                                                                                    'Employee Status': 'employeeStatus',
                                                                                    'Business Line': 'businessLine',
                                                                                    'Business Sub-Line': 'subBusinessLine',
                                                                                    'Geographic Region': 'region',
                                                                                    'Office Location': 'city',
                                                                                    'Career Level': 'title'})

    ## Select and reorder columns
    talentDF['name'] = talentDF['firstName'] + ' ' + talentDF['lastName']
    talentDF = talentDF[['email', 'name', 'employeeStatus',
                         'businessLine', 'subBusinessLine', 'title',
                         'region', 'city']]

    loadDF = updateDF.merge(talentDF, how='left', on='email')

    # Insert date and status fields
    loadDF['reportingDate'] = reportingDate
    loadDF['status'] = loadDF.apply(lambda row: 'Left Firm - Talent Data' if pd.isnull(row['employeeStatus'])  # Return value if employeeStatus is null (did not join)
                                                else row['employeeStatus'], axis=1)  # Return employeeStatus as default value
    loadDF = loadDF.fillna('User Data Not Found')

    # Realign columns to match report
    loadDF = loadDF[['reportingDate', 'email', 'name',
                     'employeeStatus', 'businessLine','subBusinessLine',
                     'title', 'region', 'city', 'status',
                     'timeSaved', 'numberOfClicks']]

    # Write previous data to archive
    lastReportDF = pd.read_csv(f"data/report/{currentReportName}")
    lastReportDF.to_csv(f"data/archive/upslide-report-{reportingDate}.csv", index=False)

    # Union latest data (for practitioners not in latest data, leave past data untouched)
    updatedReportDF = pd.concat([lastReportDF, loadDF]).reset_index(drop=True)
    updatedReportDF.to_csv("data/report/upslide-report.csv", index=False)
