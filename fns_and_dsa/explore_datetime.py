from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime("Current date and time: %Y-%m-%d %H:%M:%S")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    return future_date.strftime("Future date: %Y-%m-%d")

print(calculate_future_date())
print(display_current_datetime())
