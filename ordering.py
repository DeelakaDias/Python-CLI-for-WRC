import time
import os


# System should display the championship standings ordered by points in descending order.
def VCT():
    try:
        driver_file = open("Driver_details_Draft.txt", 'r')
        # checking if driver_file ia empty or not
        if os.path.getsize("Driver_details_Draft.txt") == 0:
            time.sleep(1.0)
            print("You need to execute RFF")
            time.sleep(1.0)
            print("You will direct to main menu")
            time.sleep(1.5)

        else:
            read_for_order = driver_file.readlines()
            driver_file.close()
            list_for_comparing = []
            for line in read_for_order:
                edit_line = line.strip().split(",")
                list_for_comparing.append(edit_line)

            print(list_for_comparing)
            # sorting driver details according to the driver score
            for i in range(len(list_for_comparing)):
                for k in range(i + 1, len(list_for_comparing)):
                    if int(list_for_comparing[i][4]) > int(list_for_comparing[k][4]):
                        list_for_comparing[i], list_for_comparing[k] = list_for_comparing[k], list_for_comparing[i]

            list_for_comparing.reverse()

            # adding sorted driver details to the table
            from tabulate import tabulate
            head = ["Name", "Age", "Team", "Car", "Points"]
            time.sleep(1.0)
            print(tabulate(list_for_comparing, headers=head, tablefmt="fancy_grid").center(100))
            time.sleep(1.0)
            print("Driver details sorted")
            time.sleep(1.0)

    except FileNotFoundError:
        time.sleep(0.5)
        print("First you need to execute STF")
        time.sleep(0.5)
        print("You will direct to main menu")
        time.sleep(1.0)

# sorting function refered, https://tutorial.eyehunts.com/python/how-to-sort-a-list-in-python-without-sort-function-example-code/

