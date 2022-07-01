# UPDATE THESE VARIABLES #

## MAY DATA
USAGE_FILE_NAME = "Deloitte Canada FA UpSlide User Data May 2022.xlsx"
TALENT_FILE_NAME = "FA Headcount Report_RITM2192044.xlsx"
CURRENT_REPORT_NAME = "upslide-report.csv"
REPORTING_DATE = "2022-05-31"  # YYYY-MM-DD format

# UPDATE THOSE VARIABLES #

from scripts.UpdateEmployees import update_employee_csv
from scripts.UpdateLicenses import get_license_data
from scripts.UpdateUsage import update_report_csv

update_employee_csv(TALENT_FILE_NAME)
get_license_data()
update_report_csv(USAGE_FILE_NAME, TALENT_FILE_NAME, CURRENT_REPORT_NAME, REPORTING_DATE)
