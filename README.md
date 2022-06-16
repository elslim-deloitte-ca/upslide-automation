# upslide-automation

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
    config/\*
  
    config/\*\*/\*
  
    data/\*
  
    data/\*\*/\*
  
