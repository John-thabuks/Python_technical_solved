'''No of days per month. The first value 0 is just a placeholder for indexing'''
#Leap year has February with 29 days
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    '''This function will return true if its leap year and false if not a leap year.'''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    '''return number of days in that month in that year'''
    if not 1 <= month <= 12:
        return "Invalid month."
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


year =int(input("INsert the year to check if it's leap year: "))
month = int(input("Which month number do you wish to confirm number of days: "))
print(f"Is the year leap :) : {is_leap(year)}")
print(days_in_month(year, month))