#!/usr/bin/python3.4
from sense_hat import SenseHat
from time import sleep

sense=SenseHat()

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
        print("Forecast for: ", self.listdays, sep='\t')

        self.maxday = len(self.listdays) - 1

        day = self.listdays[self.d]
        for key in self.result[day].keys():
            self.daytimes.append(key)
        self.daytimes.sort(key=int)

        self.maxhour = len(self.daytimes) - 1

    def changeday(self):
        self.daytimes = []
        self.h = 0
        day = self.listdays[self.d]
        for key in self.result[day].keys():
            self.daytimes.append(key)
        self.daytimes.sort(key=int)

        self.maxhour = len(self.daytimes) - 1

    def __del__(self):
        sense.clear()
        print("\n\t\tClean up complete!")

    def checkday(self, max):
        sense.show_letter(str(self.d), text_colour=(255, 0, 255))
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
        sense.show_letter(str(self.h), text_colour=(140,200,70))
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
        sense.show_letter(str(self.d), text_colour=(255,0,255))

    def daydown(self):
        self.d -= 1
        sense.show_letter(str(self.d), text_colour=(255, 0, 255))

    def timeup(self):
        self.h += 1
        sense.show_letter(str(self.h), text_colour=(140,200,70))

    def timedown(self):
        self.h -= 1
        sense.show_letter(str(self.h), text_colour=(140,200,70))

    def showweather(self):
        day = self.listdays[self.d]
        hour = self.daytimes[self.h]
        final = self.result[day][hour]
        wID = final["ID"]
        wTemp = final["Temperature"]
        finaloutput(wID, wTemp)

# sense.set_rotation(270)

# Colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
orange = (255,165,0)
magenta = (255,0,255)
cyan = (0,255,255)
white = (255,255,255)
black = (0,0,0)
wordsgreen = (114, 255, 148)

w1 = (50, 0, 180)
w2 = (100, 0, 140)
w3 = (0, 50, 150)
w4 = (0, 40, 255)
w5 = (0, 100, 255)
w6 = (0, 145, 255)
w7 = (0, 190, 255)
w8 = (150, 255, 255)
w9 = cyan
w10 = green
w11 = yellow
w12 = orange
w13 = red

O = white
X = red
C = green
B = black

creeper_pixels = [
    C, C, C, C, C, C, C, C,
    C, C, C, C, C, C, C, C,
    C, B, B, C, C, B, B, C,
    C, B, B, C, C, B, B, C,
    C, C, C, B, B, C, C, C,
    C, C, B, B, B, B, C, C,
    C, C, B, B, B, B, C, C,
    C, C, B, C, C, B, C, C
]

questionMark = [
    O, O, O, X, X, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, O, O, X, O, O,
    O, O, O, O, X, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, O, O, O, O
]

def testprint(tsleep):
    # Print message
    sense.show_message("Weather App", 0.05, red, white)
    sleep(tsleep)
    sense.clear()

def print_txt(text, scroll_speed):
    sense.show_message(text, scroll_speed, wordsgreen, black)
    sense.clear()

def showtext(text):
    sense.show_letter(str(text), text_colour = magenta)
    sleep(0.5)
    sense.clear()

def img_creeperSSS(tsleep):

    # Print Picture
    sense.set_pixels(creeper_pixels)

    sleep(tsleep)
    sense.clear()

def img_qnmark(tsleep):
    sense.set_pixels(questionMark)

    sleep(tsleep)
    sense.clear()

# Print image by specifying link
def img_link(link ,tsleep):
    sense.load_image("/home/pi/pi_weatherLED_project_don/img" + link)

    sleep(tsleep)
    sense.clear()

# Display weather information on Sensehat when called by main application
def finaloutput(wID, wTemp):
    # Thunderstorm
    if 200 <= wID <= 232:
        print_wTemp(wTemp)
        tstorm_animation()

    # Drizzle
    elif 300 <= wID <= 321:
        print_wTemp(wTemp)
        slowrain_animation()

    # Raining
    elif 500 <= wID <= 531:
        print_wTemp(wTemp)
        rain_animation()

    # Snow
    elif 600 <= wID <= 622:
        print_wTemp(wTemp)
        snow_animation()

    # Misty/Foggy
    elif 701 <= wID <= 781:
        print_wTemp(wTemp)
        haze_animation()

    # Clear Sky/ Sunny
    elif 800 <= wID <= 801:
        print_wTemp(wTemp)
        sun_animation()

    # Clouds
    elif 802 <= wID <= 804:
        print_wTemp(wTemp)
        cloud_animation()

    # No image available for this weather condition yet
    # Only Extreme weather condition will get this image (e.g. tornado, hurricane)
    else:
        print_wTemp(wTemp)
        img_qnmark(2)

# Changes colour according to temperature
def print_wTemp(wTemp):
    scroll_speed = 0.08
    if -20 >= wTemp:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w1, black)
    elif -15 > wTemp >= -20:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w2, black)
    elif -10 > wTemp >= -15:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w3, black)
    elif -5 > wTemp >= -10:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w4, black)
    elif 0 > wTemp >= -5:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w5, black)
    elif 5 > wTemp >= 0:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w6, black)
    elif 10 > wTemp >= 5:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w7, black)
    elif 15 > wTemp >= 10:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w8, black)
    elif 20 > wTemp >= 15:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w9, black)
    elif 25 > wTemp >= 20:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w10, black)
    elif 30 > wTemp >= 25:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w11, black)
    elif 35 > wTemp >= 30:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w12, black)
    elif wTemp >= 35.0:
        sense.show_message("Temp: " + str(wTemp), scroll_speed, w13, black)
    else:
        sense.show_message("FAIL", scroll_speed)
    sense.clear()

# Animate 2 frames
def animate2(cc1, cc2, count, tsleep):
    for x in range(0, count):
        if x % 2 == 0:
            sense.load_image(cc1)
        else:
            sense.load_image(cc2)
        sleep(tsleep)

# Animate 3 frames
def animate3(cc1, cc2, cc3, count, tsleep):
    chgfc = 1
    for x in range(0, count):
        if chgfc == 1:
            sense.load_image(cc1)
            chgfc = 2
        elif chgfc == 2:
            sense.load_image(cc2)
            chgfc = 3
        else:
            sense.load_image(cc3)
            chgfc = 1
        sleep(tsleep)

# Weather animations
def rain_animation():

    sense.low_light = True

    anim1 = "/home/pi/pi_weatherLED_project_don/img/rain_1.png"
    anim2 = "/home/pi/pi_weatherLED_project_don/img/rain_2.png"
    anim3 = "/home/pi/pi_weatherLED_project_don/img/rain_3.png"

    speed = 0.1
    count = 6/speed

    chgfc = 1

    for x in range(0, int(count)):
        if chgfc == 1:
            sense.load_image(anim1)
            chgfc = 2
        elif chgfc == 2:
            sense.load_image(anim2)
            chgfc = 3
        else:
            sense.load_image(anim3)
            chgfc = 2
        sleep(speed)

    sense.clear()

def slowrain_animation():
    sense.low_light = True

    anim1 = "/home/pi/pi_weatherLED_project_don/img/rain_1.png"
    anim2 = "/home/pi/pi_weatherLED_project_don/img/rain_2.png"
    anim3 = "/home/pi/pi_weatherLED_project_don/img/rain_3.png"

    speed = 0.25
    count = 6/speed

    chgfc = 1

    for x in range(0, int(count)):
        if chgfc == 1:
            sense.load_image(anim1)
            chgfc = 2
        elif chgfc == 2:
            sense.load_image(anim2)
            chgfc = 3
        else:
            sense.load_image(anim3)
            chgfc = 2
        sleep(speed)

    sense.clear()

def cloud_animation():
    sense.low_light = True

    anim1 = "/home/pi/pi_weatherLED_project_don/img/claracloud_1.png"
    anim2 = "/home/pi/pi_weatherLED_project_don/img/claracloud_2.png"

    speed = 0.25
    count = 5/speed

    animate2(anim1, anim2, int(count), speed)
    sense.clear()

def sun_animation():
    sense.low_light = True

    anim1 = "/home/pi/pi_weatherLED_project_don/img/sun3_1.png"
    anim2 = "/home/pi/pi_weatherLED_project_don/img/sun3_2.png"
    anim3 = "/home/pi/pi_weatherLED_project_don/img/sun3_3.png"

    speed = 0.25
    count = 5/speed

    chgfc = 1
    round = True

    for x in range(0, int(count)):
        if chgfc == 1:
            sense.load_image(anim1)
            chgfc = 2
            round = True
        elif chgfc == 2:
            sense.load_image(anim2)
            if round:
                chgfc = 3
            else:
                chgfc = 1
        else:
            sense.load_image(anim3)
            chgfc = 2
            round = False
        sleep(speed)

    sense.clear()

def snow_animation():
    sense.low_light = True

    anim1 = "/home/pi/pi_weatherLED_project_don/img/snow_1.png"
    anim2 = "/home/pi/pi_weatherLED_project_don/img/snow_4.png"
    anim3 = "/home/pi/pi_weatherLED_project_don/img/snow_3.png"

    speed = 0.25
    count = 6 / speed

    chgfc = 1
    round = True
    last = count - 3

    # Snow animation
    for x in range(0, int(count)):
        # 1 '42' '43'
        if chgfc == 1:
            sense.load_image(anim1)
            chgfc = 2
        elif chgfc == 2:
            sense.load_image(anim2)
            chgfc = 3
        else:
            sense.load_image(anim3)
            chgfc = 1

        sleep(speed)

    sense.clear()

def haze_animation():
    sense.low_light = True

    anim1 = "/home/pi/pi_weatherLED_project_don/img/haze_1.png"
    anim2 = "/home/pi/pi_weatherLED_project_don/img/haze_2.png"

    speed = 0.6
    count = 6/speed

    animate2(anim1, anim2, int(count), speed)
    sense.clear()

def tstorm_animation():
    sense.low_light = True

    anim = ["/home/pi/pi_weatherLED_project_don/img/tstorm_1.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_2.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_3.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_4.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_5.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_6.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_7.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_8.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_9.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_10.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_11.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_12.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_13.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_14.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_15.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_16.png",
            "/home/pi/pi_weatherLED_project_don/img/tstorm_17.png",
            ]

    chgfc = 1
    flash = False
    round = 3
    animate = True

    # Thunder animation very complicated
    # Part 1 & 2 & 3 of Thunder animation
    # Flash is for the 2nd part of lightning flicker
    # Part 1 and 3 is lightning appear and disappear
    while animate:
        if chgfc == 1:
            if flash:
                if round != 0:
                    sense.load_image(anim[7])
                else:
                    flash = False
            # elif round == 0:
            #     sense.load_image(animp3_1)
            else:
                sense.load_image(anim[0])
            chgfc = 2
        elif chgfc == 2:
            if flash:
                if round != 0:
                    sense.load_image(anim[8])
            elif round == 0:
                sense.load_image(anim[10])
            else:
                sense.load_image(anim[1])
            chgfc = 3
        elif chgfc == 3:
            if flash:
                if round != 0:
                    sense.load_image(anim[9])
                    round = round - 1
                    chgfc = 1
            elif round == 0:
                sense.load_image(anim[11])
                chgfc = 4
            else:
                sense.load_image(anim[2])
                chgfc = 4
        elif chgfc == 4:
            if round == 0:
                sense.load_image(anim[12])
            else:
                sense.load_image(anim[3])
            chgfc = 5
        elif chgfc == 5:
            if round == 0:
                sense.load_image(anim[13])
            else:
                sense.load_image(anim[4])
            chgfc = 6
        elif chgfc == 6:
            if round == 0:
                sense.load_image(anim[14])
            else:
                sense.load_image(anim[5])
            chgfc = 7
        elif chgfc == 7:
            if round == 0:
                sense.load_image(anim[15])
            else:
                sense.load_image(anim[6])
            chgfc = 8
        else:
            if round == 0:
                sense.load_image(anim[16])
                animate = False
            else:
                sense.load_image(anim[7])
                flash = True
            chgfc = 1

        sleep(0.1)

    sense.clear()

# Joystick weather information display
def joystickweather(result):
    wc = WeatherController(result)
    print("\n\tSelect the data you want to output using the joystick\n\tUp/Down -> Select Day\tLeft/Right -> Select Time\n\t2x Middle -> Show Weather\tLong Press Middle -> Stop\n")

    doing = True
    cleanup = False
    middle = 0
    while doing:
        event = sense.stick.wait_for_event()
        if event.action == "pressed":
            if event.direction == "up":
                middle = 0
                if not wc.checkday(True):
                    wc.dayup()
                    wc.changeday()
            elif event.direction == "down":
                middle = 0
                if not wc.checkday(False):
                    wc.daydown()
                    wc.changeday()
            elif event.direction == "left":
                middle = 0
                if not wc.checktime(False):
                    wc.timedown()
            elif event.direction == "right":
                middle = 0
                if not wc.checktime(True):
                    wc.timeup()
            # Double press middle to print
            else:
                middle += 1
                if middle == 2:
                    print("\nDisplaying forecast for: ", "Date: " + wc.listdays[wc.d], "Time: " + wc.daytimes[wc.h] + ":00", sep="\t")
                    wc.showweather()
                    middle = 0

        elif event.action == "released":
            continue

        # Stop animation
        elif event.action == "held":
            if event.direction == "up":
                if not wc.checkday(True):
                    wc.dayup()
                    wc.changeday()
            elif event.direction == "down":
                if not wc.checkday(False):
                    wc.daydown()
                    wc.changeday()
            elif event.direction == "left":
                if not wc.checktime(False):
                    wc.timedown()
            elif event.direction == "right":
                if not wc.checktime(True):
                    wc.timeup()
            else:
                cleanup = True

        if cleanup:
            del wc
            doing = False

    print("\t\tFinish!\n")