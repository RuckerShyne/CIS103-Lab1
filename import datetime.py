import datetime

today = datetime.datetime.today().date()

dob = datetime.date(month, day, year)

try:

year = input('Enter numerical Year: ')

month = input('Enter numerical Month: ')

day = input('Enter numerical Day: ')

age_result = ageCalculator(int(year), int(day), int(month))

print(f'You are {age_result} years old')