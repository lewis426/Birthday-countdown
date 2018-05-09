# import necessary modules
import datetime


# create functions
def print_header():
    # title
    print('-----------------------------------')
    print('        BIRTHDAY COUNTDOWN')
    print('-----------------------------------')
    print()


def get_birthday_from_user():
    d=datetime.date.today()
    # user inputs
    print('When were you born?')
    while True:
        try:
            year = int(input('Which year were you born?[YYYY]: '))
        except ValueError:
            print('Please type a numerical input.')
            continue
        if d.year < year or year < 1900:
            print('Please enter a valid year. Try Again.')
            continue
        else:
            break
    while True:
        try:
            month = int(input('Which month were you born?[MM]: '))
        except ValueError:
            print('Please type a numerical input.')
            continue
        if 0 > month or month > 12 :
            print('Not a valid month. Try Again.')
            continue
        elif d.year == year and month > d.month:
            print('Please enter a date in the past.')
            continue
        else:
            break
    while True:
        try:
            day = int(input('Which day were you born?[DD]: '))
        except ValueError:
            print('Please type a numerical input.')
            continue
        if 0 > day or day > 31:
            print('Not a valid day. Try Again.')
            continue
        elif year == d.year and month == d.month and day > d.day:
            print('Please enter a date in the past.')
            continue
        else:
            break
    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(year=target_date.year, month=original_date.month, day=original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print('Your birthday was {0} days ago!'.format(-days))
    elif days > 0:
        print('Your birthday is in {0} days!'.format(days))
    else:
        print('It is your birthday.')


def main():
    cmd = "Yes"
    while cmd.lower().strip() != 'no':
        try:
            while cmd.lower().strip() != 'yes' and cmd.lower().strip() != 'no':
                try:
                    print('Please enter yes or no')
                    cmd = input('Would you like to restart (\'Yes or No?\'):')
                    continue
                except ValueError:
                    print('Please enter a valid value')
                    continue
            if cmd.lower().strip() == 'yes':
                print_header()
                bday = get_birthday_from_user()
                print('Your date of birth is {0}'.format(bday))
                today = datetime.date.today()
                num_of_days = compute_days_between_dates(bday, today)
                print_birthday_information(num_of_days)
                cmd = input('Would you like to restart (\'Yes or No?\'):')
            else:
                print('Goodbye')
        except ValueError:
            print('Please enter a valid value')


main()
