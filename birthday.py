from datetime import datetime

birthday = "1-May-12"


raw_date = "1-May-12"
date_format = "%d-%B-%y"

# Read the date

parsed_date = datetime.strptime(birthday, date_format)
print(parsed_date)

date_str = parsed_date.strftime("%-m/%-d/%Y") # 01/11/17
print(date_str)