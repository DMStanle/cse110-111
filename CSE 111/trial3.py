import datetime
from datetime import datetime

obj = datetime.now()
year = obj.year
new_obj = obj.replace(year=2035)
day_of_week = obj.weekday()

print(new_obj)
print(day_of_week)