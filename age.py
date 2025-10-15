from datetime import datetime


def ask_user_for_number(message, min, max):
    n = input(message)

    is_number = False
    while not is_number:
        try:
            n = int(n)
            if n >= min and n <= max:
                is_number = True
            else:
                print("That is not in the valid range...")
                n = input("Please try again: ")
        except:
            print("That is not a number...")
            print("Please try again: ")
    return n


def calculate_age(input_date):
    current_date = datetime.now()

    current_timestamp = current_date.timestamp()
    input_timestamp = input_date.timestamp()

    difference = current_timestamp - input_timestamp
    years = difference // (365 * 24 * 60 * 60)

    return (int)(years)


def ask_date_separately():
    print("Please input a date...")
    _day = ask_user_for_number("Day: ", 1, 31)
    _month = ask_user_for_number("Month: ", 1, 12)
    _year = ask_user_for_number("Year: ", 1, 2025)

    return datetime(day=_day, month=_month, year=_year)


def ask_date_together():
    input_date = input("Please input a date in DD-MM-YYYY format: ")
    return datetime.strptime(input_date, "%d-%m-%Y")


def main():
    # input_date = ask_date_separately()
    input_date = ask_date_together()

    age = calculate_age(input_date)

    print(age)


if __name__ == "__main__":
    main()
