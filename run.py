"""Travelbooka imports"""
# import random to generate random free extras
import random

# os import to clear terminal for user
import os

# import datetime module to work with holiday date
from datetime import datetime, timedelta

# google drive api and google sheets imports and constants
import gspread
from google.oauth2.service_account import Credentials

# pyfiglet import to generate logo in ASCII
import pyfiglet

# import colorama for adding colour
from colorama import Fore
from colorama import init

# import tabulate to display data in tables
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Travelbooka")

init(autoreset=True)


def logo_display():
    """
    App logo and description
    """
    logo = pyfiglet.figlet_format(
        "Travelbooka", font="standard", justify="center")
    print(logo)

    print(Fore.RED + "Create".center(20) + Fore.MAGENTA + "your".center(20) +
          Fore.CYAN + "own".center(20) + Fore.YELLOW + "travel".center(20)
          + "\n")

    print("\033[1m" + "Welcome to Travelbooka. Please follow the prompts to "
          "create your unique booking. \n" + "\033[1m")
    print("To proceed after each input, please press Enter on your keyboard."
          "\n")


def validate_date(entry):
    """
    Checks if user entered date meets program requirements
    and returns error if not
    """
    
    try:
        date_condition1 = datetime.today().date() + timedelta(days=3)
        date_condition2 = datetime.today().date() + timedelta(days=365)
        entry_parsed = datetime.strptime(entry, '%Y-%m-%d').date()
        if entry_parsed < date_condition1:
            raise ValueError(
                "Enter a date that is at least 3 days from now.\n"
                f"Booking cannot be made for entered date {entry}, \n"
                "because it's either in the past or too soon"
            )
        if entry_parsed > date_condition2:
            raise ValueError(
                "Enter a date that is within 1 year from now.\n"
                f"Booking cannot be made for entered date {entry}, \n"
                "because it is more than 1 year from now"
            )
    except ValueError as error:
        print(Fore.RED + f"Invalid data: {error}, please try again.\n")
        return False
    return True

def validate_budget(entry):
    """
    Checks if user entered budget figure meets program requirements
    and returns error if not
    """
    try:
        if entry < 230:
            raise ValueError(
                "The minimum budget needed is 230.\n"
                "It's not possible to create a package for this budget"
                f"{entry}"
            )
    except ValueError as error:
        print(Fore.RED + f"Invalid data: {error}, please try again.\n")
        return False
    return True


def validate_selection(value, options):
    """
    Checks if user selected options is within the available scope
    """
    try:
        if value not in options:
            raise ValueError(
                f"Selected value of {value} is not available. \n"
                f"Choose available value from displayed options"
            )
    except ValueError as error:
        print(Fore.RED + f"Invalid data: {error}.\n")
        return False
    return True


def date_input():
    """
    Takes user desired travel date, stores it in a global variable
    to be used to determine Activity holidays type, if Activity holidays
    are selected
    """
    while True:
        date_entry = input("Enter a date in YYYY-MM-DD format: " + "\n")

        if validate_date(date_entry):
            break

    month_entry = int(date_entry.split('-')[1])

    global season
    summer = [4, 5, 6, 7, 8, 9]
    if month_entry in summer:
        season = "summer"
        return season
    else:
        season = "winter"
        return season


def budget_input():
    """
    Takes user target budget, stores it in a variable
    to be used during offer selection, validates if entry meets
    program requirements (at least 230)
    """
    while True:
        try:
            global budget_entry
            budget_entry = int(input("Enter your target budget in number format: "
                           + "\n" + "EUR "))
            if budget_entry < 230:
                raise ValueError(
                    "The minimum budget needed is 230.\n"
                    "It's not possible to create a package for this budget"
                    f"{budget_entry}")
            break
        except ValueError as error:
            print(Fore.RED + f"Invalid data: {error}, please try again.\n")
            continue

    return budget_entry


def people_count():
    """
    Takes user information on the amount of people going, checks
    if the entry meets amount and format restrictions (num between 1 - 11)
    """
    global people_entry
    while True:
        try:
            people_entry = int(input("Enter number of people on the booking: "
                               + "\n"))
            if people_entry < 1:
                raise ValueError(
                    "The minimum number of people is 1.\n"
                    f"It's not possible to create a package for this entry {people_entry}")
            if people_entry > 11:
                raise ValueError(
                    "The maximum number of people is 11.\n"
                    f"It's not possible to create a package for {people_entry} people.")
            break
        except ValueError as error:
            print(Fore.RED + f"Invalid data: {error}, please try again.\n")
            continue
        

    return people_entry



def get_holiday_types():
    """
    Displays holiday types from google sheet, takes month_entry as an argument,
    takes user selected holiday type input and validates duration for type
    2 & 3
    """
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    holiday_types = SHEET.worksheet("holiday_types")
    data = holiday_types.get_all_values()

    headers = data[0]
    t_body = data[1:]
    print(tabulate(t_body, headers=headers, tablefmt="fancy_grid") + "\n")

    global selected_type
    global duration

    while True:
        selected_type = int(input("Choose holiday type by entering code from "
                                  "table: " + "\n"))
        if validate_selection(selected_type, [1, 2, 3]):
            break

    if selected_type == 2:
        while True:
            duration = int(input("Choose duration according to the table: "
                                 + "\n"))
            if validate_selection(duration, [3, 5, 7]):
                break
        print(Fore.GREEN + f"You selected {data[selected_type][1]} with "
              f"duration of {duration} days.\n")
        return [data[selected_type][1], duration]
    elif selected_type == 3:
        while True:
            duration = int(input("Choose duration according to the table: "
                                 + "\n"))
            if validate_selection(duration, [3, 5, 7]):
                break
        if season == "summer":
            print(Fore.GREEN + f"You selected Summer {data[selected_type][1]} "
                  f"with duration of {duration} days.\n")
            return [data[selected_type][1], duration]
        else:
            print(Fore.GREEN + f"You selected Winter {data[selected_type][1]} "
                  f"with duration of {duration} days.\n")
            return [data[selected_type][1], duration]
    else:
        duration = 3
        print(Fore.GREEN + f"You selected {data[selected_type][1]} with "
              "duration of 3 days.\n")
        return [data[selected_type][1], duration]


def get_package():
    """
    Calculates available packages from data in flight_offer and hotel_offer
    sheets and parameters entered previously by the user
    compares offered packages to user entered budget, displays packages within
    user budget range in a table
    """

    flight_offer = SHEET.worksheet("flight_offer")
    flights = flight_offer.get_all_values()

    hotel_offer = SHEET.worksheet("hotel_offer")
    hotels = hotel_offer.get_all_values()

    # get indexes of targeted columns instead of entering a set number
    col_names = hotels[0]
    price_index = int(col_names.index("Hotel\nDay\nRate")) + 1
    code_index = int(col_names.index("Hol Code")) + 1
    hotel_name_index = int(col_names.index("Hotel")) + 1
    location_index = int(col_names.index("Location")) + 1
    season_index = int(col_names.index("Season")) + 1

    # get values from targeted columns, remove or store required headers
    price_list = hotel_offer.col_values(price_index)
    price_list_header = price_list.pop(0)
    code_list = hotel_offer.col_values(code_index)
    del code_list[0]
    hotel_list = hotel_offer.col_values(hotel_name_index)
    hotel_list_header = hotel_list.pop(0)
    location_list = hotel_offer.col_values(location_index)
    location_list_header = location_list.pop(0)
    season_list = hotel_offer.col_values(season_index)
    del season_list[0]
    summer_indices = [i for i, value in enumerate(season_list) if
                      value == "summer"]
    winter_indices = [i for i, value in enumerate(season_list) if
                      value == "winter"]

    # create int lists for params needed in calculation
    int_code_list = [eval(code) for code in code_list]
    int_price_list = [eval(price) for price in price_list]

    # headers for basic package table
    package_headers = ["Airline", "Flight\nPrice", hotel_list_header,
                       location_list_header, price_list_header,
                       "Total\nPackage\nPrice"]

    # get flights depending on holiday type
    if selected_type == 1:
        airline = flights[1][4]
        flight_price = int(flights[1][3])
    elif selected_type == 2:
        airline = flights[3][4]
        flight_price = int(flights[2][3])
    else:
        airline = flights[2][4]
        flight_price = int(flights[3][3])

    target_indices_unordered = []

    # get common items from selected holiday codes and hotel prices
    for code, price in zip(int_code_list, int_price_list):
        if code == selected_type and (price * duration * people_entry) <= (
                                      budget_entry - (
                                          flight_price * people_entry)):
            price_index = [i for i, value in enumerate(int_price_list) if
                           value == price]
            code_index = [i for i, value in enumerate(int_code_list) if
                          value == code]
            target_index = list(set.intersection(*map(set, [price_index,
                                code_index])))
            target_indices_unordered.append(target_index)

    target_indices_list = [item for sublist in target_indices_unordered for
                           item in sublist]

    target_index_list = []

    # verifying season from input date for the selected trip
    if selected_type == 3:
        if season == "summer":
            new_list = list(set.intersection(*map(set, [target_indices_list,
                            summer_indices])))
            [target_index_list.append(x) for x in new_list if x not in
             target_index_list]
        else:
            new_list = list(set.intersection(*map(set, [target_indices_list,
                            winter_indices])))
            [target_index_list.append(x) for x in new_list if x not in
             target_index_list]
    else:
        [target_index_list.append(x) for x in target_indices_list if x not in
         target_index_list]

    nested_table = []

    # loop through available indexes to create the basic package table
    for index in target_index_list:
        hotel_name = hotel_list[index]
        location = location_list[index]
        hotel_price = int_price_list[index]
        package_price = (flight_price + (hotel_price * duration
                                         )) * people_entry
        table_row = [[airline, flight_price, hotel_name, location, hotel_price,
                     package_price]]
        nested_table.append(table_row[-index:])

    table = [item for sublist in nested_table for item in sublist]

    # exits program if no packages available in the budget range
    if table == []:
        print(Fore.RED + f"There are no available packages of this type "
              f"({selected_type}) with duration of {duration} days witin the "
              f"entered budget range of {budget_entry}")
        exit()

    print("Here are the packages available for your entered budget")

    print(tabulate(table, headers=package_headers, tablefmt="fancy_grid",
          showindex="always") + "\n")

    selected_package = int(input("Choose your package by entering the number "
                           "in the first column: ") + "\n")

    # clear terminal to avoid clutter
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    print(Fore.GREEN + "\n" + f"You selected package {selected_package}"
          + "\n")
    selection = table[selected_package]
    selection_table = [selection]
    print(tabulate(selection_table, headers=package_headers,
          tablefmt="fancy_grid") + "\n")

    return [selected_package, selection[3], selection[2], selection[0],
            selection[5]]


def add_free_extras():
    """
    Selects random extras from the free extras lists to be
    added to the booking
    """
    free_extras = SHEET.worksheet("free_extras")
    extras_data = free_extras.get_all_values()
    col_names = extras_data[0]
    extra_name_index = int(col_names.index("Type")) + 1
    extra_names = free_extras.col_values(extra_name_index)
    del extra_names[0]
    random_extra = random.choice(extra_names)

    print(Fore.GREEN + "As a way of saying thanks for booking with us")
    print(Fore.YELLOW + "we added the below free extra to your package")
    print(Fore.MAGENTA + f"{random_extra}")

    return random_extra


class Booking:
    """
    Creates and instance of booking and adds to the bookings sheet, creates
    a unique booking id by incrementing list of Booking refs from bookings tab
    in Google sheet
    """
    bookings_sheet = SHEET.worksheet("bookings")
    last_id = len(bookings_sheet.col_values(1))

    def __init__(self, trip_type, t_duration, location, hotel, airline,
                 p_price, free_extras):
        self.id = self.last_id
        self.trip_type = trip_type
        self.t_duration = t_duration
        self.location = location
        self.hotel = hotel
        self.airline = airline
        self.p_price = p_price
        self.free_extras = free_extras

    def update_worksheet(self):
        """
        Adds the new booking to bookings tab
        """
        bookings_sheet = SHEET.worksheet("bookings")

        def __str__(self):
            return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.trip_type,
                                                       self.t_duration,
                                                       self.location,
                                                       self.hotel,
                                                       self.airline,
                                                       self.p_price,
                                                       self.free_extras)

        bookings_sheet.append_row(__str__(self).split(","))

    def confirm_booking(self):
        """
        Returns booking id to user and informs to contact if they want to
        purchase
        """
        print("\n\n" + "\033[1m" + "YOUR UNIQUE BOOKING REFERENCE IS "
              + "\033[1m")
        booking_ref = pyfiglet.figlet_format(str(self.id), font="bubble")
        print(Fore.GREEN + f"{booking_ref}")
        print(Fore.MAGENTA + "Give us a call, if you'd like to purchase your "
              "booking")


def main():
    """
    Run all program functions
    """
    logo_display()
    date_input()
    people_count()
    budget_input()
    type_duration = get_holiday_types()
    selected_package = get_package()
    free_extras = add_free_extras()
    booking = Booking(type_duration[0], type_duration[1],
                      selected_package[1], selected_package[2],
                      selected_package[3],
                      selected_package[4], free_extras)
    booking.update_worksheet()
    booking.confirm_booking()


if __name__ == "__main__":
    main()
