import datetime

current_date = datetime.date.today()

year  = int(input("What is the year of your birthday?\n"))
month = int(input("What is the month of your birthday?\n"))
day   = int(input("What is the day of your birthday?\n"))

my_birthday = datetime.date(year, month, day)

difference = my_birthday - current_date
days_difference = difference.days

print(f"My birthday is in {days_difference} days!")