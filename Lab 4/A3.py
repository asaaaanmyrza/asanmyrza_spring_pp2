from datetime import datetime, timedelta

def drop_microseconds(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')


current_datetime = datetime.now()
datetime_without_microseconds = drop_microseconds(current_datetime)
print("microseconds:", current_datetime)
print(" without microseconds:", datetime_without_microseconds)