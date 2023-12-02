driver_details = []
iteration_time = 1
import time
import adding
import deleting
import updating
import ordering
import simulating
import random_for_vrl
import saving
import file_handling


def display():
    print("WORLD RALLY CROSS CHAMPIONSHIP MANAGEMENT".center(100))
    print("Type ADD for adding driver detail".center(100))
    print("Type DDD for deleting".center(100))
    print("Type UDD for updating driver details".center(100))
    print("Type VCT for viewing the rally cross standings table".center(100))
    print("Type SRR for simulating a random race".center(100))
    print("Type VRL for viewing race table sorted according to the date".center(100))
    print("Type STF to save the current data to a text file".center(100))
    print("Type RFF to load data from the saved text file".center(100))
    print("Type ESC to exit the program".center(100))
    print()


while True:
    display()
    opt = input("Enter the option: ")

    if opt == "ADD":
        adding.ADD()
        iteration_time += 1
        continue

    elif opt == "DDD":
        deleting.DDD()

    elif opt == "UDD":
        updating.UDD()

    elif opt == "VCT":
        ordering.VCT()

    elif opt == "SRR":
        simulating.SRR()

    elif opt == "STF":
        saving.STF()

    elif opt == "VRL":
        random_for_vrl.VRL()

    elif opt == "RFF":
        file_handling.RFF()

    elif opt == "ESC":

        opinion = input("Are you sure you want terminate from program, yes or no: ")
        if opinion == "yes":
            driver_file = open("Driver_details_Draft.txt", 'w')
            driver_file.close()
            break
        else:
            continue

    else:
        time.sleep(0.5)
        print("Invalid Input")
        time.sleep(1.0)
        continue