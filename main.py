# UPDATE THESE VARIABLES #

USAGE_FILE_NAME = "Deloitte Canada FA UpSlide User Data April 2022.xlsx"
TALENT_FILE_NAME = "FA Headcount report_RITM2154626.xlsx"
CURRENT_REPORT_NAME = "upslide-report.csv"
REPORTING_DATE = "2022-05-31"  # YYYY-MM-DD format

# UPDATE THOSE VARIABLES #

from scripts.LicenseScraper import get_license_data
from scripts.UpdateUsage import update_report_csv

get_license_data()
update_report_csv(USAGE_FILE_NAME, TALENT_FILE_NAME, CURRENT_REPORT_NAME, REPORTING_DATE)
