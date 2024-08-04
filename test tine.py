from datetime import datetime, timedelta

def get_days_difference(date_list):
    # Filter out empty strings and None values
    cleaned_dates = [date for date in date_list if date is not None and date.strip() != ""]
    print(cleaned_dates)
    if not cleaned_dates:
        return None
    
    # Convert the dates to datetime objects
    datetime_dates = [datetime.strptime(date, '%d.%m.%y') for date in cleaned_dates]
    
    # Get the latest date from the list
    latest_date = max(datetime_dates)
    
    # Calculate the difference between the latest date and today
    difference = datetime.now() - latest_date
    
    # Return the difference in days
    return difference.days

# Example usage
dates_list = ['01.01.22', '  ', '15.02.23', None, '05.03.24']
days_difference = get_days_difference(dates_list)
print("Days difference:", days_difference)
