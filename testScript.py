import gwModules as gw
import time
import csv

appid = gw.getAppID()

runFlag = True
operFlag = None
weather = None

while runFlag == True:
    operFlag = input("Choose which operation you would like to run:\n  Run all cities by typing [all]\n  Run a list of cities by typing [list]\n  Run one single city [one]\n   ->")
    timeFlag = input("Time the ")

    if operFlag == 'all':
        cityIDfile = input("Enter city IDs list file path.\n ->")
        cityArray = []
        with open(cityIDfile) as f:
            tempCities = csv.reader(f, delimiter=',')
            for row in tempCities:
                  cityArray.append(int(''.join(row)))
        ti = time.time()
        gw.allCities(cityArray, appid)
        tf = time.time()
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
        ti = time.time()
        weather = gw.getCityWeather(cityArray, "array", appid)
        tf = time.time()
        print(weather)
        runFlag = False

    elif operFlag == 'one':
        cityID = input("Enter city ID.\n ->")
        ti = time.time()
        weather = gw.getCityWeather(cityID, "string", appid)
        tf = time.time()
        print(weather)
        runFlag = False

    else:
        print("\nInvalid entry. Be sure to type your operation mode exactly as specified.\n\n")
        time.sleep(2)

deltaT = tf -ti
print(f"\n\nDone in {deltaT}s.\n")
