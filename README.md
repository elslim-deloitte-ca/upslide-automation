# UpSlide Automation

## How to run
1. Move the monthly usage Excel file into data/raw/usage
2. Move the monthly talent data into data/raw/talent
3. Open the main.py file in the project repository
4. Change the variables for USAGE_FILE_NAME and TALENT_FILE_NAME to match the file names you just moved over
5. Change REPORTING_DATE to the last day of the previous month. E.g. if today is 2022 June 16, set REPORTING_DATE to 2022-05-31
6. Right click main.py and click "Run 'main'"
7. Wait until you see "Process finished" in the terminal output



## How to perform the first time setup
**GitHub: To access the scripts**
1. Navigate to https://github.com/elslim-deloitte-ca/upslide-automation
2. Click on the HTTPS button and copy the URL

**PyCharm: To execute the scripts**
1. Download and install PyCharm Community Edition from https://www.jetbrains.com/pycharm/download/#section=windows
2. Once installed, click "Get from VCS"
3. Paste the URL copied from Step 2 under GitHub above
4. Select the directory you want to work with in the Directory drop down

**Environment setup**
1. Within the newly opened project, create 2 folders called *config* and *data*
2. Within config, create a new file called *upslide-credentials.json*
3. In the new file, add copy and paste the following: 

```
  {
     "USER": "example@deloitte.ca",
     "PASSWORD": "password123"
  }
```

4. Replace the email address and password values with your UpSlide admin portal credentials
5. Within data, create *archive*, *processed*, *raw*, and *report* subfolders
6. Within raw, create *talent* and *usage* subfolders

**Installing dependencies**
1. Navigate to LicenseScraper.py and UpdateUsage.py within the scripts folder
2. For the first few lines that start with either *import* or *from*, right click any red text, hover over "Context actions" and click install package
3. Repeat for both files

**Check .gitignore**
1. Open the .gitignore file located in the main project folder
2. Ensure the following lines are included at the top of the file:
```
  config/*
  config/**/*
  data/*
  data/**/*
```

## Maintenance
### Talent report requests
1. Create ServiceNow ticket for a Talent Data Report
2. In Report Type, select *Other Report*
3. Enter the following into the description field
```
Please provide details
Combined headcount and change report to understand details of current employees. Employees who left the firm should not be included in this report Refer to RITM2154626 for past request
```
4. In the field asking for additional information, add
```
Please indicate if any additional information is required. Please be as specific as possible.
Fields requested: * Employee email * Employee name * Employee title (e.g. Senior Associate, Quick Start Analyst, Manager) * Employee team (e.g. M&VA - Value Advisory, FOR - Disputes & Litigation) * Region (e.g. Atlantic, Ontario, etc.) * City (e.g. Toronto, Montreal) * Employment status (e.g. Active, Left the Firm) Refer to RITM2154626 for past request
```
5. In the field asking for dates used, enter
```
Fields should contain most recent title/team (e.g. an analyst from Vancouver promoted to senior in Toronto in the last 12 months should show as a senior from Toronto).
```
6. When asked if data will be shared external to Talent, select yes and state:
```
Intended audience and distribution: Internal Deloitte practitioners only. For technology license management purposes.
```
7. In additional comments, add:
```
Previously reviewed and approved by Yonette Creavalle - RITM 2098403 Previously delivered as per RITM2154626
```


### UpSlide report requests
Email sent to Anastasiya and Reed from the UpSlide team. Excel sheet attached to response


### Chrome and Chromedriver Updates 
When Google Chrome on the Deloitte laptop updates, there may be a need to update chromedriver.exe. In this case, navigate to https://chromedriver.chromium.org/downloads and replace the .exe file with the one matching the requested version







