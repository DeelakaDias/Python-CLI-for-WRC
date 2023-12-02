import time
# System will allow the user to enter the driver details by prompting the required information
def ADD():
    driver_file = open("Driver_details_Draft.txt", 'a')
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
            driver_age = input("Enter driver's age: ")
            if not driver_age.isdigit():
                print("You can't enter letter for age")
                continue
            driver_age = int(driver_age)
            if 16 <= driver_age < 60:
                driver_details.append(str(driver_age))
                break
            else:
                print("Age must in between 16 to 60")
                continue
        except ValueError:
            print("You can't leave this blank")
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
    driver_file.close()
    time.sleep(1.0)
    print("Driver added")
    time.sleep(1.0)
