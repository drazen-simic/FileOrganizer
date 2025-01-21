from datetime import datetime, timedelta, date

# Current date and time
current_datetime = datetime.now()
print(f"Current date and time: {current_datetime}")

# Create specific date
specific_date = datetime(2023, 12, 25, 10, 30, 0)
print(f"Specific date: {specific_date}")

# Format dates
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date: {formatted_date}")

# Date calculations
tomorrow = current_datetime - timedelta(days=1)
next_week = current_datetime + timedelta(weeks=1)
two_hours_later = current_datetime + timedelta(hours=2)
print(tomorrow)
# Date components
print(f"Year: {current_datetime.year}")
print(f"Month: {current_datetime.month}")
print(f"Day: {current_datetime.day}")
print(f"Hour: {current_datetime.hour}")
print(f"Minute: {current_datetime.minute}")

# Parse string to datetime
date_string = "2023-12-25 10:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

# Compare dates
today = date.today()
is_future = specific_date > current_datetime
is_past = specific_date < current_datetime

# Time between dates
time_difference = specific_date - current_datetime
print(f"Days until Christmas: {time_difference.days}")

# Get day of week (0 = Monday, 6 = Sunday)
weekday = current_datetime.weekday()
print(f"Day of week: {weekday}")

# Get ISO calendar info (year, week number, weekday)
iso_calendar = current_datetime.isocalendar()
print(f"ISO calendar: Year {iso_calendar[0]}, Week {iso_calendar[1]}")

# Check if year is leap year
is_leap = date(current_datetime.year, 1, 1).replace(year=current_datetime.year).strftime("%Y").isleap()
print(f"Is leap year: {is_leap}")

# Get first and last day of current month
first_day = current_datetime.replace(day=1)
last_day = (first_day.replace(month=first_day.month % 12 + 1, day=1) - timedelta(days=1))
print(f"First day of month: {first_day}")
print(f"Last day of month: {last_day}")