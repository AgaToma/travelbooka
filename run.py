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
from colorama import Fore
colorama.init(autoreset=True)

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

    print("Welcome to Travelbooka. Please follow the prompts to create your unique booking. \n")
    print("To proceed after each input, please press Enter on your keyboard. \n")



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
    budget_entry = input("Enter your target budget in number format: " + "EUR ")
    return budget_entry

def people_count():
    """
    Takes user information on the amount of people going
    """
    people_entry = input("Enter number of people on the booking: " + "\n")
    return people_entry

def display_hol_types():
    """
    Displays holiday types from google sheet
    """
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    holiday_types = SHEET.worksheet("holiday_types")
    data = holiday_types.get_all_values()

    col_names = data[0]
    print(col_names)




logo_display() 
date_input()
people_count()
budget_input()
display_hol_types()

