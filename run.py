# google drive api and google sheets imports and constants
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Travelbooka")

# os import to clear terminal for user
import os

# pyfiglet import to generate logo in ASCII
import pyfiglet

# import colorama for adding colour
import colorama
from colorama import Fore, Back
from colorama import init
init(autoreset=True)

# import datetime module to work with holiday date
import datetime

# import tabulate to display data in tables
from tabulate import tabulate


def logo_display():
    """
    App logo and description
    """
    logo = pyfiglet.figlet_format(
        "Travelbooka", font="standard", justify="center")
    print(logo)

    print(Fore.RED + "Create".center(20) + Fore.MAGENTA + "your".center(20) +
    Fore.CYAN + "own".center(20) + Fore.YELLOW + "travel".center(20) + "\n")

    print("\033[1m" + "Welcome to Travelbooka. Please follow the prompts to create your unique booking. \n" + "\033[1m")
    print("To proceed after each input, please press Enter on your keyboard. \n")

user_month = 0

def date_input():
    """
    Takes user desired travel date, stores it in a variable
    to be used to determine Activity holidays type, if Activity holidays
    are selected
    """
    date_entry = input("Enter a date in YYYY-MM-DD format: " + "\n")
    user_month = date_entry.split('-')[1]
    
    return user_month

def budget_input():
    """
    Takes user target budget, stores it in a variable
    to be used during offer selection
    """
    global budget_entry
    budget_entry = int(input("Enter your target budget in number format: " + "\n" + "EUR "))
    return budget_entry

def people_count():
    """
    Takes user information on the amount of people going
    """
    global people_entry
    people_entry = int(input("Enter number of people on the booking: " + "\n"))
    return people_entry

def get_holiday_types():
    """
    Displays holiday types from google sheet, 
    takes user selected holiday type and validates duration for type 2 & 3
    """
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    holiday_types = SHEET.worksheet("holiday_types")
    data = holiday_types.get_all_values()

    headers = data[0]
    t_body = data[1:] 
    print(tabulate(t_body, headers=headers, tablefmt="fancy_grid") + "\n")

    global selected_type
    global duration

    selected_type = int(input("Choose holiday type by entering code from table: " + "\n")) 
    
    if selected_type == 2:
        duration = int(input("Choose duration according to the table: " + "\n"))
        print(Fore.GREEN + f"You selected {data[selected_type][1]} with duration of {duration} days.\n")
        return [selected_type, duration]
    elif selected_type == 3:
        duration = int(input("Choose duration according to the table: " + "\n"))
        summer = [4,5,6,7,8,9]
        if user_month in summer:
            print(Fore.GREEN + f"You selected Summer {data[selected_type][1]} with duration of {duration} days.\n")
            return [selected_type, duration]
        else:
            print(Fore.GREEN + f"You selected Winter {data[selected_type][1]} with duration of {duration} days.\n")
            return [selected_type, duration]
    else:
        duration = 3
        print(Fore.GREEN + f"You selected {data[selected_type][1]} with duration of 3 days.\n")
        return [selected_type, duration]
    
    print("Thanks for your selection. We are getting your basic package...")



def basic_package():
    flight_offer = SHEET.worksheet("flight_offer")
    flights = flight_offer.get_all_values()

    hotel_offer = SHEET.worksheet("hotel_offer")
    hotels = hotel_offer.get_all_values()
    col_names = hotels[0]
    price_index = int(col_names.index("Price/day/person eur")) + 1
    code_index = int(col_names.index("Hol Code")) + 1
    price_list = hotel_offer.col_values(price_index)
    del price_list[0]
    code_list = hotel_offer.col_values(code_index)
    del code_list[0]
    int_code_list = [eval(code) for code in code_list]
    int_price_list = [eval(price) for price in price_list]
    

    print("Here is your basic package")
    if selected_type == 1:
        print(flights[1][4])
        flight_price = flights[1][3]
    elif selected_type == 2:
        print(flights[2][4])
        flight_price = flights[2][3]
    else:
        print(flights[3][4])
        flight_price = flights[3][3]

    for code, price in zip(int_code_list, int_price_list):
        if code == selected_type and (price * duration * people_entry) < budget_entry:
            print(price)
        else:
            print("Not working")








def main():
    logo_display() 
    date_input()
    people_count()
    budget_input()
    get_holiday_types()
    basic_package()


main()



