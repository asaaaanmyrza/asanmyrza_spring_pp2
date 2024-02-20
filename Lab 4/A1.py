from datetime import datetime, timedelta
def whereiam(n):
    current_time = datetime.now()
    return current_time - timedelta(n)

print(whereiam(5))