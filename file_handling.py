import time
import os


def RFF():
    try:
        driver_file_save = open("Final_file.txt", 'r')
        # checking if driver_file ia empty or not
        if os.path.getsize("Final_file.txt") == 0:
            time.sleep(1.0)
            print("Nothing to load to the main program")
            time.sleep(0.5)
            print("You will direct to main menu")

        else:
            read = driver_file_save.readlines()
            driver_file = open("Driver_details_Draft.txt", 'w')
            for line in read:
                driver_file.write("".join(line))
        print("Data loaded to the main program")
        time.sleep(1.0)
        print("You will jump to the main program")
        time.sleep(1.0)

    except FileNotFoundError:
        time.sleep(0.5)
        print("First you need to execute STF")
        time.sleep(0.5)
        print("You will direct to main menu")
        time.sleep(1.0)