#!/usr/bin/python3.4
import pyowmWeather
import senseLED
import pwli

from sense_hat import SenseHat
from time import sleep
import json

# sense = SenseHat()
#
# sense.set_rotation(270)
#
# # # Print message
# # sense.show_message("Hello world")
#
# # Colours
# red = (255,0,0)
# green = (0,255,0)
# blue = (0,0,255)
# yellow = (255,255,0)
# magenta = (255,0,255)
# cyan = (0,255,255)
# white = (255,255,255)
#
# # sense.clear(off)
#
# # Display Single Character
# sense.show_letter("A")
#
# sleep(0.5)
#
# sense.clear()
#
# X = [255, 0, 0]  # Red
# O = [255, 255, 255]  # White
#
# question_mark = [
# O, O, O, X, X, O, O, O,
# O, O, X, O, O, X, O, O,
# O, O, O, O, O, X, O, O,
# O, O, O, O, X, O, O, O,
# O, O, O, X, O, O, O, O,
# O, O, O, X, O, O, O, O,
# O, O, O, O, O, O, O, O,
# O, O, O, X, O, O, O, O
# ]
#
# sense.set_pixels(question_mark)

# senseLED.testprint()

# for arg in sys.argv[1:]:
#     print(arg)
#     senseLED.printtxt(arg, 1)

# senseLED.testpicture(1)

# def animate2(cc1, cc2):
#     for x in range(0, 30):
#         if x % 2 == 0:
#             sense.load_image(cc1)
#         else:
#             sense.load_image(cc2)
#         sleep(0.35)
#
# def animate3(cc1, cc2, cc3):
#     chgfc = 1
#     for x in range(0, 30):
#         if chgfc == 1:
#             sense.load_image(cc1)
#             chgfc = 2
#         elif chgfc == 2:
#             sense.load_image(cc2)
#             chgfc = 3
#         else:
#             sense.load_image(cc3)
#             chgfc = 1
#         sleep(0.3)

# sense=SenseHat()

# anim1 = "/home/pi/project/img/clarascloud_1.png"
# anim2 = "/home/pi/project/img/clarascloud_2.png"

# anim1 = "/home/pi/pi_weatherLED_project_don/img/rain_1.png"
# anim2 = "/home/pi/pi_weatherLED_project_don/img/rain_2.png"
# anim3 = "/home/pi/pi_weatherLED_project_don/img/rain_3.png"
#
# sense.set_rotation(270)
#
# animate3(anim1, anim2, anim3)
# sense.clear()

# senseLED.rain_animation()
# senseLED.slowrain_animation()

print('sep')

abc = SenseHat()

doing = True
waitinput = True

while doing:
    if waitinput == True:
        print("\n\tWaiting for user to input... \n")
    event = abc.stick.wait_for_event()
    print("The joystick was {} {}".format(event.action, event.direction))

    if event.action == "pressed":
        waitinput = False
        if event.direction == "up":
            senseLED.rain_animation()
        elif event.direction == "down":
            senseLED.snow_animation()
        elif event.direction == "left":
            senseLED.tstorm_animation()
        elif event.direction == "right":
            senseLED.slowrain_animation()
    elif event.action == "released":
        waitinput = True
        if event.direction == "up":
            senseLED.sun_animation()
        elif event.direction == "down":
            senseLED.cloud_animation()
        elif event.direction == "right":
            senseLED.haze_animation()
    # Stop animation
    elif event.action == "held":
        if event.direction == "middle":
            doing = False

    abc.clear()
    sleep(1)

senseLED.img_creeperSSS(2)

# location = "ueki"
# output = pyowmWeather.getfullfweather(location)
# # result = json.loads(output[1])
# result = output[1]
# print(result)
# json.dumps(result, indent=4, sort_keys=True)

# abc = SenseHat()
# result = {'1/20': {'12': {'ID': 500, 'Temperature': 2.49}, '0': {'ID': 800, 'Temperature': -0.91}, '3': {'ID': 800, 'Temperature': 8.97}, '6': {'ID': 800, 'Temperature': 11.27}, '18': {'ID': 500, 'Temperature': 3.03}, '9': {'ID': 802, 'Temperature': 5.3}, '15': {'ID': 500, 'Temperature': 1.91}, '21': {'ID': 500, 'Temperature': 3.35}}, '1/19': {'12': {'ID': 803, 'Temperature': -0.05}, '0': {'ID': 800, 'Temperature': 0.1}, '3': {'ID': 800, 'Temperature': 9.85}, '6': {'ID': 800, 'Temperature': 10.74}, '18': {'ID': 800, 'Temperature': -4.89}, '9': {'ID': 802, 'Temperature': 4.94}, '15': {'ID': 800, 'Temperature': -1.7}, '21': {'ID': 800, 'Temperature': -6.63}}, '1/18': {'12': {'ID': 800, 'Temperature': -0.56}, '0': {'ID': 500, 'Temperature': 6.27}, '3': {'ID': 500, 'Temperature': 8.2}, '6': {'ID': 800, 'Temperature': 10.11}, '18': {'ID': 800, 'Temperature': -4.48}, '9': {'ID': 800, 'Temperature': 5.64}, '15': {'ID': 800, 'Temperature': -3.17}, '21': {'ID': 800, 'Temperature': -5.46}}, '1/16': {'9': {'ID': 801, 'Temperature': 11.98}, '12': {'ID': 500, 'Temperature': 11.7}, '21': {'ID': 501, 'Temperature': 8.27}, '15': {'ID': 500, 'Temperature': 12.18}, '18': {'ID': 501, 'Temperature': 10.6}}, '1/17': {'12': {'ID': 500, 'Temperature': 5.0}, '0': {'ID': 500, 'Temperature': 8.32}, '3': {'ID': 501, 'Temperature': 10.2}, '6': {'ID': 500, 'Temperature': 10.47}, '18': {'ID': 500, 'Temperature': 4.93}, '9': {'ID': 500, 'Temperature': 8.69}, '15': {'ID': 500, 'Temperature': 5.11}, '21': {'ID': 500, 'Temperature': 4.4}}}
#
# class WeatherController:
#     # Class variables
#     listdays = []
#     d = 0
#     h = 0
#     daytimes = []
#     dchange = True
#     cleanup = False
#     selected = False
#
#     def __init__(self, output):
#         self.result = output
#         for key in self.result.keys():
#             listdays.append(key)
#         listdays.sort()
#         print(listdays)
#
#
# listdays = []
# for key in result.keys():
#     listdays.append(key)
# listdays.sort()
# print(listdays)
#
# # # Cleanup
# # del CLASS
#
# # for day in listdays:
# #     daytimes = []
# #     for key in result[day].keys():
# #         daytimes.append(key)
# #     daytimes.sort(key=int)
# #     print(daytimes)
#
# # Globals
# doing = True
# d = 0
# h = 0
# daytimes = []
# dchange = True
# cleanup = False
# selected = False
# print("\n\tSelect the data you want to output using the joystick\n \tUP/DOWN: Change the day\n \tLEFT/RIGHT: Change the time\n")
#
# maxday = len(listdays) - 1
#
# while doing:
#     if cleanup:
#         doing = False
#         abc.clear()
#
#     if dchange:
#         day = listdays[d]
#         for key in result[day].keys():
#             daytimes.append(key)
#         daytimes.sort(key=int)
#         print(daytimes)
#         dchange = False
#
#     event = abc.stick.wait_for_event()
#     print("The joystick was {} {}".format(event.action, event.direction))
#
#     if event.action == "pressed":
#         if event.direction == "up":
#             if d == maxday:
#                 print("Stop! It is already at the last day!")
#             else:
#                 d = d + 1
#                 dchange = True
#         elif event.direction == "down":
#             if d == 0:
#                 print("Stop! It is already at the first day!")
#             else:
#                 d = d - 1
#                 dchange = True
#         elif event.direction == "left":
#             if h == 0:
#                 print("Stop! It is already at the earliest timing!")
#             else:
#                 h = h - 1
#         elif event.direction == "right":
#             if h == len(daytimes) - 1:
#                 print("Stop! It is already at the latest timing!")
#             else:
#                 h = h + 1
#         else:
#             selected = True
#
#     elif event.action == "released":
#         if event.direction == "up":
#             senseLED.sun_animation()
#
#     # Stop animation
#     elif event.action == "held":
#         if event.direction == "middle":
#             cleanup = True
#
# print("\n\t\tFinish!\n")

# sense=SenseHat()
# # Colours
# red = (255,0,0)
# green = (0,255,0)
# blue = (0,0,255)
# yellow = (255,255,0)
# orange = (255,165,0)
# magenta = (255,0,255)
# cyan = (0,255,255)
# white = (255,255,255)
# black = (0,0,0)
#
# w1 = (50, 0, 180)
# w2 = (100, 0, 140)
# w3 = (0, 50, 150)
# w4 = (0, 40, 255)
# w5 = (0, 100, 255)
# w6 = (0, 145, 255)
# w7 = (0, 190, 255)
# w8 = (150, 255, 255)
# w9 = cyan
# w10 = green
# w11 = yellow
# w12 = orange
# w13 = red
#
# for x in range(0,13):
#     if x == 0:
#         sense.show_message(str(x), text_colour=w1)
#     elif x == 1:
#         sense.show_message(str(x), text_colour=w2)
#     elif x == 2:
#         sense.show_message(str(x), text_colour=w3)
#     elif x == 3:
#         sense.show_message(str(x), text_colour=w4)
#     elif x == 4:
#         sense.show_message(str(x), text_colour=w5)
#     elif x == 5:
#         sense.show_message(str(x), text_colour=w6)
#     elif x == 6:
#         sense.show_message(str(x), text_colour=w7)
#     elif x == 7:
#         sense.show_message(str(x), text_colour=w8)
#     elif x == 8:
#         sense.show_message(str(x), text_colour=w9)
#     elif x == 9:
#         sense.show_message(str(x), text_colour=w10)
#     elif x == 10:
#         sense.show_message(str(x), text_colour=w11)
#     elif x == 11:
#         sense.show_message(str(x), text_colour=w12)
#     elif x == 12:
#         sense.show_message(str(x), text_colour=w13)