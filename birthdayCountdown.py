import datetime

def get_user_birthday():
    print('What is your birthday please?')
    year = int(input('Please enter the year [YYYY]: '))
    month = int(input('Please enter the month[MM]: '))
    day = int(input('Please enter the day[DD]: '))
    birthday = datetime.datetime(year, month, day)
    return birthday

def compute_birthday_difference(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    difference = date1 - date2
    days = int(difference.total_seconds()/60/60/24)
    return days

def print_bday_info(days):
    if days < 0:
        print('Your birthday is in {} days.'.format(-days))
    elif days > 0:
        print('Your birthday was {} days ago. Hope it was great!'.format(days))
    else:
        print('Happy Birthday!')

def main():
    bday = get_user_birthday()
    now = datetime.datetime.now()
    days = compute_birthday_difference(bday, now)
    print_bday_info(days)

main()
