#!/usr/bin/python3.4
import pyowmWeather
import senseLED
import sys
from datetime import datetime

def finaloutput(wID, wTemp):
    # Thunderstorm
    if 200 <= wID <= 232:
        senseLED.print_wTemp(wTemp, 0.1)
        senseLED.tstorm_animation()

    # Drizzle
    elif 300 <= wID <= 321:
        senseLED.print_wTemp(wTemp, 0.1)
        senseLED.slowrain_animation()

    # Raining
    elif 500 <= wID <= 531:
        senseLED.print_wTemp(wTemp, 0.1)
        senseLED.rain_animation()

    # Snow
    elif 600 <= wID <= 622:
        senseLED.print_wTemp(wTemp, 0.1)
        senseLED.snow_animation()

    # Misty/Foggy
    elif 701 <= wID <= 781:
        senseLED.print_wTemp(wTemp, 0.1)
        senseLED.haze_animation()

    # Clear Sky/ Sunny
    elif 800 <= wID <= 801:
        senseLED.print_wTemp(wTemp, 0.1)
        senseLED.sun_animation()

    # Clouds
    elif 802 <= wID <= 804:
        senseLED.print_wTemp(wTemp, 0.1)
        senseLED.cloud_animation()

    # No image available for this weather condition yet
    # Only Extreme weather condition will get this image (e.g. tornado, hurricane)
    else:
        senseLED.print_wTemp(wTemp, 0.15)
        senseLED.img_qnmark(2)

def printerror():
    #Global Error message
    cwusage = "GET CURRENT WEATHER DETAILS\n This will output the current weather details  (mainly temperature and weather condition) through the Raspberry Pi SenseHat module.\n\n Usage: python3 pwli.py current [location]\n Example: python3 pwli.py current kumamoto\n"
    fwusage = "GET FORECAST WEATHER DETAILS\n This will output the forecast weather details which the user can choose. Note that the forecast timing is 3-hourly so the program will only accept the time input in multiples of 3. The forecast details are also limited to 4 days in advance.\n\n Usage: python3 pwli.py 3hfc [location] [How many days from current date (0-4)] [time]\n Example: python3 pwli.py 3hfc kumamoto 2 6"
    print(cwusage, fwusage, sep='\n')
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
            # Location not found
            if result == False:
                print("Location not found!")
                senseLED.img_creeperSSS(2)
            # SUCCESS
            else:
                wID = result[1]
                wTemp = result[2]
                finaloutput(wID, wTemp)

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
                            print("Checking the forecasted weather for '" + sys.argv[2] + "'\n")
                            result = pyowmWeather.get3hfweather(sys.argv[2], sys.argv[3], sys.argv[4])
                            # Location not found
                            if result == False:
                                print("Location not found!")
                                senseLED.img_creeperSSS(2)
                            else:
                                wID = result[1]
                                wTemp = result[2]
                                finaloutput(wID, wTemp)
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
                            finaloutput(wID, wTemp)
                else:
                    print("Please only enter days within the range 0-4\n")
                    senseLED.img_creeperSSS(2)
            else:
                print("\tPlease only enter time in multiples of 3.\n")
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