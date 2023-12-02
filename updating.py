import time
import os


# System should allow user to delete a driver by searching by name
def UDD():
    try:
        driver_file = open("Driver_details_Draft.txt", 'r')
        # checking if driver_file ia empty or not
        if os.path.getsize("Driver_details_Draft.txt") == 0:
            time.sleep(1.0)
            print("First you need enter driver details")
            time.sleep(0.5)
            print("You will direct to main menu")

        else:
            while True:
                driver_name = input("Enter the name of the driver you want to update: ")
                if not driver_name.replace(" ", "").isalpha():
                    print("You are not allowed to type numbers here or leave this blank")
                    continue
                else:
                    break

            while True:
                try:
                    driver_team = input("Enter the team of the driver: ")
                    break
                except None:
                    print("You are not allowed leave this blank")
                    continue

            # reading line of the file from the main file
            driver_file = open("Driver_details_Draft.txt", 'r')
            read = driver_file.readlines()
            driver_file.close()
            driver_file = open("Driver_details_Draft.txt", 'w')
            found = False

            for line in read:
                edit_line = line.strip().split(",")

                if (driver_name == edit_line[0]) and (driver_team == edit_line[2]):
                    time.sleep(1.0)
                    print("Next onwards enter the details you want to update")
                    found = False
                    driver_details = []

                    while True:
                        driver_name = input("Enter driver's name: ")
                        if not driver_name.replace(" ", "").isalpha():
                            # to check if driver_name contain number,https://www.w3schools.com/python/ref_string_isalpha.asp
                            print("You are not allowed to type numbers here or leave this blank")
                            continue
                        driver_details.append(driver_name)
                        break

                    while True:
                        try:
                            driver_age = int(input("Enter driver's age: "))
                            if 16 <= driver_age < 60:
                                driver_details.append(str(driver_age))
                                break
                            else:
                                print("Age must in between 16 to 60")
                                continue
                        except ValueError:
                            print("You can't enter letter for age or leave this blank")
                            continue

                    while True:
                        try:
                            driver_team = input("Enter driver's team: ")
                            driver_details.append(driver_team)
                            break
                        except None:
                            time.sleep(0.5)
                            print("You are not allowed leave this blank")
                            continue

                    while True:
                        try:
                            driver_car = input("Enter car name: ")
                            driver_details.append(driver_car)
                            break
                        except None:
                            print("You are not allowed leave this blank")
                            continue

                    while True:
                        try:
                            driver_points = int(input("Enter points driver scored: "))
                            driver_details.append(str(driver_points))
                            break
                        except ValueError:
                            time.sleep(0.5)
                            print("You can't enter letter for score or leave this blank")
                            continue

                    driver_file.write(",".join(driver_details) + "\n")
                    time.sleep(1.0)
                    print("Driver details updated")
                    found = True

                else:
                    driver_file.write(line)

            if not found:

                time.sleep(1.0)
                print("Driver not found")
                UDD()

            driver_file.close()
            time.sleep(1.0)

    except FileNotFoundError:

        time.sleep(0.5)
        print("First you need enter driver details")
        time.sleep(0.5)
        print("You will direct to main menu")
        time.sleep(1.0)


