import time
import os


# adding points to each driver after generate randomly
def add_points(driver_details, points):
    driver_details[4] = str(int(driver_details[4]) + points)
    return driver_details


# System should simulate a random race and assign pints to each driver accordingly.
def SRR():
    import random
    try:
        driver_file = open("Driver_details_Draft.txt", 'r')
        # checking if driver_file ia empty or not
        if os.path.getsize("Driver_details_Draft.txt") == 0:
            time.sleep(1.0)
            print("First you need enter driver details")
            time.sleep(0.5)
            print("You will direct to main menu")

        else:
            location_list = ["Nyirád", "Höljes", "Montalegre", "Barcelona", "Rīga", "Norway"]
            random_location = location_list[random.randint(0, 5)]

            import random
            year = random.randint(2010, 2023)
            month = random.randint(1, 12)
            month = str(month)
            if len(month) == 1:
                month = "0" + month
            day = random.randint(1, 28)
            day = str(day)
            if len(day) == 1:
                day = "0" + day
            Date = f"{year}-{month}-{day}"
            Date = str(Date)

            race_list_draft = []
            simulate = driver_file.readlines()
            driver_file.close()
            list_for_simulate = []

            for line in simulate:
                edit_line = line.strip().split(",")
                list_for_simulate.append(edit_line)
            if len(list_for_simulate) >= 3:

                random.shuffle(list_for_simulate)
                list_for_simulate[0] = add_points(list_for_simulate[0], 10)  # add points for 1st place
                list_for_simulate[1] = add_points(list_for_simulate[1], 7)  # add points for 2nd place
                list_for_simulate[2] = add_points(list_for_simulate[2], 5)  # add points for 3rd place

                x = f"{'Position':15s}{'Name':30s}{'Team':30s}{'Points':5s}"

                position_1 = f"{str(1):15s}{(list_for_simulate[0][0]):30s}{(list_for_simulate[0][2]):30s}{str(list_for_simulate[0][4]):5s}"

                position_2 = f"{str(2):15s}{(list_for_simulate[1][0]):30s}{(list_for_simulate[1][2]):30s}{str(list_for_simulate[1][4]):5s}"

                position_3 = f"{str(3):15s}{(list_for_simulate[2][0]):30s}{(list_for_simulate[2][2]):30s}{str(list_for_simulate[2][4]):5s}"

                driver_file_1 = open("Random_Race.txt", 'a', encoding='utf-16')
                # opening the race_file in utf-16 because it contains unicodes
                driver_file_1.write("Location: ")
                driver_file_1.write(random_location+'\t\t')
                driver_file_1.write("Date: ")
                driver_file_1.write(Date+'\n \n')
                driver_file_1.write(x + '\n')
                driver_file = open("Driver_details_Draft.txt", 'w')

                for line in range(0,len(list_for_simulate)):
                    driver_file.write(",".join(list_for_simulate[line]) + "\n")
                driver_file.close()
                driver_file_1.write(position_1 + '\n')
                driver_file_1.write(position_2 + '\n')
                driver_file_1.write(position_3 + '\n')

                for j in range(3,len(list_for_simulate)):
                    position_n = f"{str(j+1):15s}{(list_for_simulate[j][0]):30s}{(list_for_simulate[j][2]):30s}{str(list_for_simulate[j][4]):5s}"
                    driver_file_1.write(position_n + "\n")

                race_file = open("Race_List.txt", 'a', encoding='utf-16')
                race_list_draft.append(random_location)
                race_list_draft.append(Date)
                driver_file_1.write("\n")
                driver_file_1.write("\n")
                race_file.write(",".join(race_list_draft) + "\n")
                race_file.close()
                driver_file_1.close()
                race_list_draft.clear()
                #time.sleep(0.5)
                print("Races were generated randomly, look for the Random Race file")
                #time.sleep(1.5)

            else:
                time.sleep(0.1)
                print("You have to enter at least 3 driver details to perform SRR")
                time.sleep(1.0)
                print("You will jump to the main program")
            time.sleep(0.5)
    except FileNotFoundError:
        time.sleep(0.5)
        print("First you need to execute STF")
        time.sleep(0.5)
        print("You will direct to main menu")
        time.sleep(1.0)