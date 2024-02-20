from datetime import datetime, timedelta
def yesterday():
    current_day = datetime.now().date() - timedelta(days=1)
    formatted_date = current_day.strftime("%a %d %B")
    return formatted_date
print(yesterday())

print(datetime.now().strftime("%a %d %B"))

def tomorrow():
    current_day = datetime.now().date() + timedelta(days=1)
    formatted_date = current_day.strftime("%a %d %B")
    return formatted_date
print(tomorrow())
