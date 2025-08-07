from datetime import datetime, timedelta
now = datetime.now()

def display_current_datetime():
    current_date = now
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date:{future_date}")


display_current_datetime()
number_of_days = int(input("Enter the number of days to add to the current date:"))
calculate_future_date()



