from datetime import datetime, timedelta

def date_difference_in_seconds(date1, date2):
    difference = date2 - date1
    return difference.total_seconds()


date_str1 = "2024-01-01 12:00:00"
date_str2 = "2024-01-01 12:30:00"

date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference in seconds:", difference_seconds)
