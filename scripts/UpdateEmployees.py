import os
import pandas as pd
from datetime import datetime
pd.set_option('display.max_columns', None)
os.chdir("../")


def update_employee_csv(latestFileName):

    employeeDF = pd.read_csv("data/report/employees.csv")

    # Archive data
    updateTS = datetime.now().strftime("%Y_%m_%d")
    employeeDF.to_csv(f"data/archive/employee_{updateTS}.csv", index=False)

    updateDF = (
        pd.read_excel(f"data/raw/talent/{latestFileName}")
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

    updateDF['name'] = (updateDF['firstName'] + ' ' + updateDF['lastName']).str.title()
    updateDF["email"] = updateDF["email"].str.lower()

    updateDF = updateDF[['email', 'name', 'employeeStatus',
                         'businessLine', 'subBusinessLine', 'title',
                         'region', 'city']].dropna()

    # Identify new employees and those who left

    joinedDF = employeeDF.merge(updateDF[["email"]].dropna(), on="email", how="outer", indicator=True)
    joinedDF["employeeStatus"] = joinedDF.apply(lambda row: "Left Firm" if row["_merge"]=="left_only" else row["employeeStatus"], axis=1)
    joinedDF.set_index("email", inplace=True)
    updateDF.set_index("email", inplace=True)
    joinedDF.update(updateDF, overwrite=False)

    joinedDF.to_csv(f"data/report/employees.csv", index=False)

    return joinedDF.reset_index(inplace=False).drop(columns=["_merge"])
