import colorama
from colorama import Fore


city = ["beirut", "tripoli", "sidon", "baalbek", "tyre", "nabatieh", "aley", "jounieh", "zahle", "zgharta", "byblos", "batroun"]

drivers = {"jad" : ["jounieh", "zahle", "zgharta"],
           "jean" : ["beirut", "tripoli", "tyre"],
           "sam" : ["byblos", "batroun", "tyre"],
           "ali" : ["baalbek", "tyre", "nabatieh"]}



def checkDelivery(drivers):
    city_name = input("Enter the city you like to deliver to: ")
    i = 1
    print("Here is the list of drivers that deliver to:", city_name.capitalize())
    for driver, cities in drivers.items():
        if city_name in cities:
            print(str(i)+".", driver.capitalize())
            i+=1
    print("-----------")
    mainMenu()



def removeCityFromDriver(drivers):
    driver_name = input("Enter driver name: ").lower()
    if driver_name not in drivers.keys():
        print(Fore.RED+"Driver does not exit")
        print(Fore.WHITE,"-----------")
        mainMenu()
    else:
        city_name = input("Enter city name: ")
        if city_name not in drivers[driver_name]:
            print(Fore.RED+"driver do not have this city")
            print(Fore.WHITE+f"-----------")
            mainMenu()
        else:
            drivers[driver_name].remove(city_name)
            print(Fore.GREEN+city_name.capitalize(), "Has been removed from the driver", driver_name.capitalize()+Fore.WHITE)
            print("-----------")
            mainMenu()




def addCityToDriver(drivers, city):
    enter_driver_name = input("Enter driver Name: ").lower()
    if enter_driver_name not in drivers.keys():
        print(Fore.RED+"driver does not exist")
        print(Fore.WHITE+"-----------")
        mainMenu()
    else:
        enter_city_name = input("Enter city name: ")
        if enter_city_name not in city:
            print(Fore.RED+"city does not exit in the main list")
            add_city = input(Fore.WHITE+"Do you want to add the city? press y to enter city, or anything to go back to main menu: ").lower()
            if add_city == "y":
                addCity()
            else:
                print("-----------")
                mainMenu()  
        elif enter_city_name in drivers[enter_driver_name]:
            print(Fore.RED+"City already exist for this driver"+Fore.WHITE)
            print("-----------")
            mainMenu()
        else:
            print("-1. To add to the begining of the route")
            print("9. To add at the end of the route")
            print("#. Enter a number to add to the given index")
            user_input = int(input("Enter the number:"))
            if user_input == -1:
                drivers[enter_driver_name].insert(0, enter_city_name)
            elif user_input == 9:
                drivers[enter_driver_name].append(enter_city_name)
            else:
                drivers[enter_driver_name].insert(user_input, enter_city_name)
            print(str(drivers).capitalize())
            print(Fore.GREEN+enter_city_name.capitalize(), "has been add to the drive", enter_driver_name.capitalize())
            print(Fore.WHITE+"-----------")
            mainMenu()




def addDriver(drivers, city):
    driver_name = input("Enter driver name:").lower()
    while True:
        try:
            driver_routes = int(input("Enter number of routes of the driver:"))
        except:
            print("Enter a number")
        else:
            break
        
    routes = []
    for i in range(driver_routes):
        routes.append(input("Enter the " + str(i+1) + " route: ").lower())
        if routes[-1] not in city:
            print(Fore.RED+routes[-1], "does not exist in city list"+Fore.WHITE)
            add_new_city = input("Do you want to add the new city? (y/n): ")
            if add_new_city == "y":
                addCity(city)
            else:
                print("-----------")
                mainMenu()
        else:    
            drivers.update({driver_name : routes})
    print(Fore.GREEN+"Driver has been added"+Fore.WHITE)
    mainMenu()



def addCity(city):
    add_city_name = str((input("Please enter the city name:")).lower())
    
    if (add_city_name.isalpha() is False) or (len(add_city_name) > 20) or (len(add_city_name) == 0):
        print(Fore.RED+"Invalid name of a city, please try again"+Fore.WHITE)
        addCity(city)
    elif add_city_name in city:
        print(Fore.RED+add_city_name.capitalize(), "already exist"+Fore.WHITE)
        print("-----------")
        mainMenu()
    else:
        city.append(add_city_name)
        print(Fore.GREEN+add_city_name.capitalize(), "has been added"+Fore.WHITE)
        print("-----------")
        mainMenu()
        return city




def mainMenu():
    print("1. To add a city")
    print("2. To add a driver")
    print("3. To add a city to the route of a driver")
    print("4. Remove a city from the driver's route")
    print("5. To check the deliverability of a package")
    print("6. Check all drivers and their routes")
    while True:
        try:
            user_input = int(input("Enter a number between 1 and 6:"))
        except:
            print(Fore.RED+"You did not enter a number between 1 and 6"+Fore.WHITE)
        else:
            break

    if user_input == 1:
        addCity(city)
    elif user_input == 2:
        addDriver(drivers, city)
    elif user_input == 3:
        addCityToDriver(drivers, city)
    elif user_input == 4:
        removeCityFromDriver(drivers)
    elif user_input == 5:
        checkDelivery(drivers)
    elif user_input == 6:
        for key, value in drivers.items():
            print(Fore.BLUE+key.capitalize(), str(value).title()+Fore.WHITE)
        mainMenu()
    else:
        print(Fore.RED+"Invalid input number, please try again"+Fore.WHITE)
        mainMenu()
    
mainMenu()