import datetime

def current_date_time():
    now = datetime.datetime.now()
    print("Current Date:", now.strftime("%d-%m-%Y"))
    print("Current Time:", now.strftime("%H:%M:%S"))

def show_date():
    date = datetime.date.today()
    print("Today's Date:", date)

def find_day():
    date = input("Enter date (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    print("Day:", date.strftime("%A"))

def calculate_difference():
    date1 = input("Enter first date (YYYY-MM-DD): ")
    date2 = input("Enter second date (YYYY-MM-DD): ")

    d1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()

    difference = abs((d2 - d1).days)
    print("Difference:", difference, "days")

def main():
    while True:
        print("\n--- Date and Time Utility ---")
        print("1. Show Current Date and Time")
        print("2. Show Today's Date")
        print("3. Find Day of a Date")
        print("4. Calculate Difference Between Dates")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            current_date_time()
        elif choice == "2":
            show_date()
        elif choice == "3":
            find_day()
        elif choice == "4":
            calculate_difference()
        elif choice == "5":
            print("Thank you for using the utility!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()