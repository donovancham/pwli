#!/usr/bin/python3.4
import pyowmWeather
import senseLED

from sense_hat import SenseHat
from time import sleep

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