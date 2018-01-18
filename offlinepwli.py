#!/usr/bin/python3.4
import pyowmWeather
import senseLED
import sys, json, os
from datetime import datetime

def updatecache(location):
    result = pyowmWeather.getfullfweather(location)
    f = open("data.txt", "w")
    f.write(str(result[1]))
    f.close()

def printerror():
    #Global Error message
    updateusage = "UPDATE WEATHER CACHE FOR LOCATION\n This will update the offline cache with the latest weather forecast for a given location.\n\n\tUsage: python3 pwli.py update [location]\n\tExample: python3 pwli.py update kumamoto\n"
    jwusage = "GET FORECAST WEATHER WITH JOYSTICK\n This allows the user to select the day and time for the weather forecast using the joystick on the Sensehat of the Raspberry Pi.\n\n\tUsage: python3 pwli.py forecast\n\tUp/Down -> Select Day\tLeft/Right -> Select Time\n\t2x Middle -> Show Weather\tLong Press Middle -> Stop"
    print(updateusage, jwusage, sep='\n')
    senseLED.img_creeperSSS(2)

def checktimedinput(input):
    t3hlist = [0, 3, 6, 9, 12, 15, 18, 21]
    for time in t3hlist:
        if int(input) == time:
            return True
    return False

def checkpasttime(input):
    currenttime = datetime.now().strftime("%-H")
    if input < int(currenttime):
        return False
    else:
        return True

print("\n########## Offline Version ##########\n")

# Check whether parameters are input correctly
if 3 >= len(sys.argv) >= 2:
    if sys.argv[1] == "forecast":
        print("Getting the forecast... \n")
        if os.stat("data.txt").st_size == 0:
            print("Data does not exist! Update cache with data first!")
            senseLED.img_creeperSSS(2)
        else:
            f = open("data.txt", "r")
            fdata = json.loads(f.readline().replace("'", "\""))
            f.close()
            senseLED.joystickweather(fdata)

    elif sys.argv[1] == "update":
        if len(sys.argv) == 3:
            print("Updating cache...\n\n")
            location = sys.argv[2]
            updatecache(location)

    else:
        printerror()
else:
    printerror()