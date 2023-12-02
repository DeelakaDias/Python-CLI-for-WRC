import time
import os
from datetime import datetime

race_list = []


# function for sorting the date
def date_str_to_datetime(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")


def VRL():
    try:
        # opening the race_file in utf-16 because it contains unicodes
        race_file = open("Race_List.txt", 'r', encoding='utf-16')
        # checking if driver_file ia empty or not
        if os.path.getsize("Race_List.txt") == 0:
            time.sleep(1.0)
            print("Unable to generate races since no driver details exists")
            time.sleep(1.0)
            print("First enter driver details and execute SRR")
            time.sleep(0.5)
            print("You will direct to main menu")

        else:
            read = race_file.readlines()
            for line in read:
                edit_line = line.strip().split(",")
                race_list.append(edit_line)

            # function calling to sort the date
            for i in range(len(race_list)):
                for k in range(i + 1, len(race_list)):
                    if date_str_to_datetime(race_list[i][1]) > date_str_to_datetime(race_list[k][1]):
                        race_list[i], race_list[k] = race_list[k], race_list[i]

            race_list.reverse()

            # adding sorted date details in a table
            from tabulate import tabulate
            head = ["Location", "Date"]
            time.sleep(1.0)
            print(tabulate(race_list, headers=head, tablefmt="fancy_grid").center(100))
            time.sleep(1.0)
            print("Driver details sorted")
            time.sleep(1.0)

    except FileNotFoundError:
        time.sleep(0.5)
        print("Since you didn't execute SRR, can't execute VRL")
        time.sleep(1.0)

# how to check whether file is empty or not https://pythonhow.com/how/check-if-a-text-file-is-empty/#:~:text=txt%20is%20empty%20if%20os,%22File%20is%20empty!%22)
