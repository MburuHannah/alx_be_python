from datetime import datetime,timedelta

def display_current_datetime():
    current_date=datetime.now()
    formatted_date=current_date.strftime("%Y-%m-%d-%H-%M-%S")
    print("Current date and time:",formatted_date)
    
   
def calculate_future_date():
    days_to_add=(int(input("Enter he number of days you want to add:")))
    current_date=datetime.now()
    future_date=current_date+timedelta(days=days_to_add)
    formatted_future_date=future_date.strftime("%Y-%m-%d")
    print("Future date after adding days:",formatted_future_date), 
    
    
display_current_datetime()
calculate_future_date()
