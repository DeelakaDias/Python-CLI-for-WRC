import time
import os


# System should be able to save the current data to a text file in a way that the data can be retrieved easily.
def STF():
    try:
        driver_file = open("Driver_details_Draft.txt", 'r')
        # checking if driver_file ia empty or not
        if os.path.getsize("Driver_details_Draft.txt") == 0:
            time.sleep(1.0)
            print("There is nothing to save")
            time.sleep(0.5)
            print("You will direct to main menu")

        else:
            driver_file_save = open("Final_file.txt", 'w')
            driver_file = open("Driver_details_Draft.txt", 'r')
            for line in driver_file:
                driver_file_save.write(line)
            driver_file = open("Driver_details_Draft.txt", 'w')
            driver_file_save.close()
            time.sleep(1.0)
            print("Data has been saved to the text file successfully")
            time.sleep(1.0)
            print("Look for the Final_file")
            time.sleep(1.0)

    except FileNotFoundError:
        time.sleep(0.5)
        print("First you need enter driver details or execute RFF")
        time.sleep(0.5)
        print("You will direct to main menu")
        time.sleep(1.0)