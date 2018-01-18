#!/usr/bin/python3.4
import pyowmWeather
import senseLED
import sys
from datetime import datetime

def printerror():
    #Global Error message
    cwusage = "GET CURRENT WEATHER DETAILS\n This will output the current weather details  (mainly temperature and weather condition) through the Raspberry Pi SenseHat module.\n\n\tUsage: python3 pwli.py current [location]\n\tExample: python3 pwli.py current kumamoto\n"
    fwusage = "GET FORECAST WEATHER DETAILS\n This will output the forecast weather details which the user can choose. Note that the forecast timing is 3-hourly so the program will only accept the time input in multiples of 3. The forecast details are also limited to 4 days in advance.\n\n\tUsage: python3 pwli.py 3hfc [location] [How many days from current date (0-4)] [time]\n\tExample: python3 pwli.py 3hfc kumamoto 2 6\n"
    jwusage = "GET FORECAST WEATHER WITH JOYSTICK\n This allows the user to select the day and time for the weather forecast using the joystick on the Sensehat of the Raspberry Pi.\n\n\tUsage: python3 pwli.py forecast [location]\n\tUp/Down -> Select Day\tLeft/Right -> Select Time\n\t2x Middle -> Show Weather\tLong Press Middle -> Stop"
    print(cwusage, fwusage, jwusage, sep='\n')
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

print("\n==============================\n")

# Check whether parameters are input correctly
if 5 >= len(sys.argv) >= 3:
    # Checking current weather
    if sys.argv[1] == "current":
        if len(sys.argv) == 3:
            print("Checking the current weather for '" + sys.argv[2] + "'\n")
            result = pyowmWeather.getcweather(sys.argv[2])
            # SUCCESS
            if result:
                wID = result[1]
                wTemp = result[2]
                senseLED.finaloutput(wID, wTemp)
            # Location not found
            else:
                print("Location not found!")
                senseLED.img_creeperSSS(2)

    # 3-hourly forecast
    elif sys.argv[1] == "3hfc":
        if len(sys.argv) == 5:
            # Check that input 4 is int between 0-24
            if checktimedinput(sys.argv[4]):
                # Check that input 3 is int in range 0-4
                if 4 >= int(sys.argv[3]) >= 0:
                    # If day is today, check time is not past
                    if int(sys.argv[3]) == 0:
                        if checkpasttime(int(sys.argv[4])):
                            print("Checking the forecasted weather for '" + sys.argv[2] + "' "  + "at " + sys.argv[4] + "00\n")
                            result = pyowmWeather.get3hfweather(sys.argv[2], sys.argv[3], sys.argv[4])
                            # Location not found
                            if result == False:
                                print("Location not found!")
                                senseLED.img_creeperSSS(2)
                            else:
                                wID = result[1]
                                wTemp = result[2]
                                senseLED.finaloutput(wID, wTemp)
                        else:
                            print("Please do not enter a time earlier than the current time.\n")
                            senseLED.img_creeperSSS(2)
                    else:
                        print("Checking the forecasted weather for '" + sys.argv[2] + "'\n")
                        result = pyowmWeather.get3hfweather(sys.argv[2], sys.argv[3], sys.argv[4])
                        # Location not found
                        if result == False:
                            print("Location not found!")
                            senseLED.img_creeperSSS(2)
                        else:
                            wID = result[1]
                            wTemp = result[2]
                            senseLED.finaloutput(wID, wTemp)
                else:
                    print("Please only enter days within the range 0-4\n")
                    senseLED.img_creeperSSS(2)
            else:
                print("\tPlease only enter time in m[]ultiples of 3.\n")
                senseLED.img_creeperSSS(2)
        else:
            printerror()

    elif sys.argv[1] == "forecast":
        if len(sys.argv) == 3:
            print("Getting the forecast for '" + sys.argv[2] + "'\n")
            result = pyowmWeather.getfullfweather(sys.argv[2])
            # SUCCESS
            if result:
                fdata = result[1]
                senseLED.joystickweather(fdata)
            # Location not found
            else:
                print("Location not found!")
                senseLED.img_creeperSSS(2)
        else:
            printerror()

    # # daily forecast
    # elif sys.argv[1] == "dailyfc":
    #     if len(sys.argv) == 4:
    #         # Check that input 3 is int in range 0-4
    #         if 14 >= int(sys.argv[3]) >= 1:
    #             result = pyowmWeather.getdailyfweather(sys.argv[2], sys.argv[3])
    #             # Location not found
    #             if result == False:
    #                 print("Location not found!")
    #                 senseLED.img_creeperSSS(2)
    #             else:
    #                 wID = result[1]
    #                 wTemp = result[2]
    #                 finaloutput(wID, wTemp)
    #         else:
    #             print("Please only enter days within the range 1-14\n")
    #             senseLED.img_creeperSSS(2)

    else:
        printerror()
else:
    printerror()