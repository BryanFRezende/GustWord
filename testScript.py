import gwModules as gw
import time
import csv

appid = gw.getAppID()

runFlag = True
operFlag = None
weather = None

while runFlag == True:
    operFlag = input("Choose which operation you would like to run:\n  Run all cities by typing [all]\n  Run a list of cities by typing [list]\n  Run one single city [one]\n   ->")
    
    if operFlag == 'all':
        cityIDfile = input("Enter city IDs list file path.\n ->")
        cityArray = []
        with open(cityIDfile) as f:
            tempCities = csv.reader(f, delimiter=',')
            for row in tempCities:
                  cityArray.append(int(''.join(row)))
        gw.allCities(cityArray, appid)
        runFlag = False

    elif operFlag == 'list':
        cityArray = []
        print("\nEnter city IDs one by one, hitting enter after each entry. Once you are finished entering city IDs, type [done] and hit enter.")
        i = None
        while i != 'done':
            i = input(' ->')
            if i != 'done':
                cityArray.append(int(i))
            else:
                break
        weather = gw.getCityWeather(cityArray, "array", appid)
        print(weather)
        runFlag = False

    elif operFlag == 'one':
        cityID = input("Enter city ID.\n ->")
        weather = gw.getCityWeather(cityID, "string", appid)
        print(weather)
        runFlag = False

    else:
        print("\nInvalid entry. Be sure to type your operation mode exactly as specified.\n\n")
        time.sleep(2)

print("\n\nDone.\n")
