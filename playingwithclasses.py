#!/usr/bin/python3.4
import pyowmWeather
import senseLED

from sense_hat import SenseHat
from time import sleep

def finaloutput(wID, wTemp):
    # Thunderstorm
    if 200 <= wID <= 232:
        senseLED.print_wTemp(wTemp)
        senseLED.tstorm_animation()

    # Drizzle
    elif 300 <= wID <= 321:
        senseLED.print_wTemp(wTemp)
        senseLED.slowrain_animation()

    # Raining
    elif 500 <= wID <= 531:
        senseLED.print_wTemp(wTemp)
        senseLED.rain_animation()

    # Snow
    elif 600 <= wID <= 622:
        senseLED.print_wTemp(wTemp)
        senseLED.snow_animation()

    # Misty/Foggy
    elif 701 <= wID <= 781:
        senseLED.print_wTemp(wTemp)
        senseLED.haze_animation()

    # Clear Sky/ Sunny
    elif 800 <= wID <= 801:
        senseLED.print_wTemp(wTemp)
        senseLED.sun_animation()

    # Clouds
    elif 802 <= wID <= 804:
        senseLED.print_wTemp(wTemp)
        senseLED.cloud_animation()

    # No image available for this weather condition yet
    # Only Extreme weather condition will get this image (e.g. tornado, hurricane)
    else:
        senseLED.print_wTemp(wTemp)
        senseLED.img_qnmark(2)

class WeatherController:
    def __init__(self, output):
        # Class variables
        self.result = output
        self.listdays = []
        self.daytimes = []
        self.d = 0
        self.h = 0
        for key in self.result.keys():
            self.listdays.append(key)
        self.listdays.sort()
        print(self.listdays)

        self.maxday = len(self.listdays) - 1

        day = self.listdays[self.d]
        for key in self.result[day].keys():
            self.daytimes.append(key)
        self.daytimes.sort(key=int)
        print(self.daytimes)

        self.maxhour = len(self.daytimes) - 1

    def changeday(self):
        self.daytimes = []
        self.h = 0
        day = self.listdays[self.d]
        for key in self.result[day].keys():
            self.daytimes.append(key)
        self.daytimes.sort(key=int)
        print(self.daytimes)

        self.maxhour = len(self.daytimes) - 1

    def __del__(self):
        abc.clear()
        print("\t\tClean up complete!\n")

    def checkday(self, max):
        print(self.d, "\n")
        abc.show_letter(str(self.d), text_colour=(255, 0, 255))
        if max:
            if self.d == self.maxday:
                print("Stop! It is already at the last day!")
                return True
        else:
            if self.d == 0:
                print("Stop! It is already at the first day!")
                return True
        return False

    def checktime(self, max):
        print(self.h, "\n")
        abc.show_letter(str(self.h), text_colour=(140,200,70))
        if max:
            if self.h == self.maxhour:
                print("Stop! It is already at the latest timing!")
                return True
        else:
            if self.h == 0:
                print("Stop! It is already at the earliest timing!")
                return True
        return False

    def dayup(self):
        self.d += 1
        abc.show_letter(str(self.d), text_colour=(255,0,255))

    def daydown(self):
        self.d -= 1
        abc.show_letter(str(self.d), text_colour=(255, 0, 255))

    def timeup(self):
        self.h += 1
        abc.show_letter(str(self.h), text_colour=(140,200,70))

    def timedown(self):
        self.h -= 1
        abc.show_letter(str(self.h), text_colour=(140,200,70))

    def showweather(self):
        day = self.listdays[self.d]
        hour = self.daytimes[self.h]
        final = self.result[day][hour]
        wID = final["ID"]
        wTemp = final["Temperature"]
        finaloutput(wID, wTemp)

abc = SenseHat()
result = {'1/20': {'12': {'ID': 500, 'Temperature': 2.49}, '0': {'ID': 800, 'Temperature': -0.91}, '3': {'ID': 800, 'Temperature': 8.97}, '6': {'ID': 800, 'Temperature': 11.27}, '18': {'ID': 500, 'Temperature': 3.03}, '9': {'ID': 802, 'Temperature': 5.3}, '15': {'ID': 500, 'Temperature': 1.91}, '21': {'ID': 500, 'Temperature': 3.35}}, '1/19': {'12': {'ID': 803, 'Temperature': -0.05}, '0': {'ID': 800, 'Temperature': 0.1}, '3': {'ID': 800, 'Temperature': 9.85}, '6': {'ID': 800, 'Temperature': 10.74}, '18': {'ID': 800, 'Temperature': -4.89}, '9': {'ID': 802, 'Temperature': 4.94}, '15': {'ID': 800, 'Temperature': -1.7}, '21': {'ID': 800, 'Temperature': -6.63}}, '1/18': {'12': {'ID': 800, 'Temperature': -0.56}, '0': {'ID': 500, 'Temperature': 6.27}, '3': {'ID': 500, 'Temperature': 8.2}, '6': {'ID': 800, 'Temperature': 10.11}, '18': {'ID': 800, 'Temperature': -4.48}, '9': {'ID': 800, 'Temperature': 5.64}, '15': {'ID': 800, 'Temperature': -3.17}, '21': {'ID': 800, 'Temperature': -5.46}}, '1/16': {'9': {'ID': 801, 'Temperature': 11.98}, '12': {'ID': 500, 'Temperature': 11.7}, '21': {'ID': 501, 'Temperature': 8.27}, '15': {'ID': 500, 'Temperature': 12.18}, '18': {'ID': 501, 'Temperature': 10.6}}, '1/17': {'12': {'ID': 500, 'Temperature': 5.0}, '0': {'ID': 500, 'Temperature': 8.32}, '3': {'ID': 501, 'Temperature': 10.2}, '6': {'ID': 500, 'Temperature': 10.47}, '18': {'ID': 500, 'Temperature': 4.93}, '9': {'ID': 500, 'Temperature': 8.69}, '15': {'ID': 500, 'Temperature': 5.11}, '21': {'ID': 500, 'Temperature': 4.4}}}

wc = WeatherController(result)

print("\n\tSelect the data you want to output using the joystick\n \tUP/DOWN: Change the day\n \tLEFT/RIGHT: Change the time\n")

doing = True
cleanup = False
middle = 0
while doing:
    event = abc.stick.wait_for_event()
    print("The joystick was {} {}".format(event.action, event.direction))

    if event.action == "pressed":
        if event.direction == "up":
            if wc.checkday(True):
                print(event.direction)
            else:
                wc.dayup()
                wc.changeday()
        elif event.direction == "down":
            if wc.checkday(False):
                print(event.direction)
            else:
                wc.daydown()
                wc.changeday()
        elif event.direction == "left":
            if wc.checktime(False):
                print(event.direction)
            else:
                wc.timedown()
        elif event.direction == "right":
            if wc.checktime(True):
                print(event.direction)
            else:
                wc.timeup()
        # Double press middle to print
        else:
            middle += 1
            if middle == 2:
                print("Output the weather information\n")
                print("\t", wc.listdays[wc.d], wc.daytimes[wc.h], sep="\t")
                wc.showweather()
                middle = 0

    elif event.action == "released":
        continue

    # Stop animation
    elif event.action == "held":
        if event.direction == "up":
            if wc.checkday(True):
                print(event.direction)
            else:
                wc.dayup()
                wc.changeday()
        elif event.direction == "down":
            if wc.checkday(False):
                print(event.direction)
            else:
                wc.daydown()
                wc.changeday()
        elif event.direction == "left":
            if wc.checktime(False):
                print(event.direction)
            else:
                wc.timedown()
        elif event.direction == "right":
            if wc.checktime(True):
                print(event.direction)
            else:
                wc.timeup()
        else:
            cleanup = True

    if cleanup:
        del wc
        doing = False

print("\n\t\tFinish!\n")