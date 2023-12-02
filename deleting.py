import time
import os


# System should allow user to delete a driver by searching by name
def DDD():
    try:
        driver_file = open("Driver_details_Draft.txt", 'r')
        # checking if driver_file ia empty or not
        if os.path.getsize("Driver_details_Draft.txt") == 0:
            # how to check whether file is empty or not https://pythonhow.com/how/check-if-a-text-file-is-empty/#:~:text=txt%20is%20empty%20if%20os,%22File%20is%20empty!%22)

            time.sleep(1.0)
            print("First you need enter driver details")
            time.sleep(0.5)
            print("You will direct to main menu")

        else:
            while True:
                user_delete_1 = input("Enter the name of the driver you want to delete: ")
                if not user_delete_1.replace(" ", "").isalpha():
                    print("You are not allowed to type numbers here")
                    continue
                else:
                    break

            user_delete_2 = input("Enter the team of the driver: ")
            # reading line of the file from the main file
            driver_file = open("Driver_details_Draft.txt", 'r')
            read = driver_file.readlines()
            driver_file.close()
            driver_file = open("Driver_details_Draft.txt", 'w')

            found = False
            for line in read:
                edit_line = line.strip().split(",")
                if (user_delete_1 == edit_line[0]) and (user_delete_2 == edit_line[2]):
                    time.sleep(1.0)
                    print("Driver deleted")
                    found = True
                else:
                    driver_file.write(line)

            if not found:
                time.sleep(1.0)
                print("Driver not found")

            driver_file.close()
            time.sleep(1.0)

    except FileNotFoundError:
        time.sleep(0.5)
        print("First you need enter driver details")
        time.sleep(0.5)
        print("You will direct to main menu")
        time.sleep(1.0)