from spartan import Spartan

all_spartans_db = {}
spartans_counter = 0


# Function to read first name
def read_firstname():
    while True:
        firstname = input("Please enter the first name: ").strip().capitalize()
        if firstname.isalnum() and len(firstname) > 1:
            break
        else:
            print("Please enter a valid name.")
    return firstname


# Function to read last name
def read_lastname():
    while True:
        lastname = input("Please enter the last name: ").strip().capitalize()
        if lastname.isalnum() and len(lastname) > 1:
            break
        else:
            print("Please enter a valid name.")
    return lastname


# Function to read year of birth
def read_birth_yeah():
    while True:
        birth_year_str = input("Please enter the year of birth (4 digits format): ")
        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
            if (birth_year > 1899) and (birth_year < 2005):
                break
            else:
                print("Please enter a year between 1900 and 2004.")
        else:
            print("Please enter a 4 digits number.")
    return birth_year


# Function to read month of birth
def read_birth_month():
    while True:
        birth_month_str = input("Please enter the month of birth (1 to 12): ")
        if birth_month_str.isdigit():
            birth_month = int(birth_month_str)
            if (birth_month > 0) and (birth_month < 13):
                break
            else:
                print("Please enter a number between 1 and 12.")
        else:
            print("Please enter a number between 1 and 12.")
    return birth_month


# Function to read day of birth
def read_birth_day():
    while True:
        birth_day_str = input("Please enter the day of birth: ")
        if birth_day_str.isdigit():
            birth_day = int(birth_day_str)
            if (birth_day > 0) and (birth_day < 32):
                break
            else:
                print("Print enter a valid number for the day of birth.")
        else:
            print("Please enter a valid number as the day of birth.")
    return birth_day


# Function to read course
def read_course():
    while True:
        course = input("Please enter the enrolled course: ").strip()
        if len(course) > 2:
            break
        else:
            print("Please enter minimum 3 characters.")
    return course


# Function to read the stream
def read_stream():
    while True:
        stream = input("Please enter the stream's name: ").strip()
        if len(stream) > 2:
            break
        else:
            print("Please enter minimum 3 characters.")
    return stream


def read_spartan_details():
    global spartans_counter
    spartans_counter += 1
    firstname = read_firstname()
    lastname = read_lastname()
    dob_day = read_birth_day()
    dob_month = read_birth_month()
    dob_year = read_birth_yeah()
    course = read_course()
    stream = read_stream()
    spartan = Spartan(spartans_counter, firstname, lastname, dob_day, dob_month, dob_year, course, stream)
    return spartan
