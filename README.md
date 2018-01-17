# Pi Weather LED Indicator (pwli)
This project makes use of the [Sensehat](https://www.raspberrypi.org/products/sense-hat/) add-on board for the Raspberry Pi to output open source weather data from [OpenWeatherMap](https://openweathermap.org/). This project is created using Pycharm.

## Usage
#### Print help
    
    python3 pwli.py
    
#### Get current weather information
    
    # python3 pwli.py current [location]
    python3 pwli.py current ueki
    
#### Get 3-hourly forecast information
**[days later]** -> Number of days later from current day *(0-4)*

**[hour of day]** -> Time of day for forecast *(0, 3, 6, 9, 12, 15, 18, 21)*
    
    # python3 pwli.py 3hfc [location] [days later] [hour of day]
    python3 pwli.py 3hfc ueki 1 12
    
#### Get forecasted weather information
Control selection by using the joystick:

- **Up/Down** -> Select the day

- **Left/Right** -> Select the time

- **Double press middle** -> display weather information through Sensehat
    
    # python3 pwli.py forecast [location]
    python3 pwli.py forecast ueki
 
## Abstract
 This is a project which I have undertaken while I was doing my internship at Kumamoto National College of Technology in Japan. Thanks to Kanzaki Sensei who provided me with a fun project to experiment with new things.

## About
The project comprises of two main components, getting the weather data and displaying it. 

### Getting weather data
Getting and processing the weather data is done by using **pyOWM** which is a python API for OpenWeatherMap. However, use of this API requires an API key and the types of weather data which a free user can get is limited. As such, this application is only able to get the current weather and the 3-hourly forecast up to 5 days in advance.

### Output
For the latter, this project makes use of the Sensehats 8x8 LED matrix shown below to display the weather information. This enables the application to play animations of different weather conditions.
![8x8 Matrix](https://www.raspberrypi.org/app/uploads/2017/05/Sense-HAT-plugged-in-1-1383x1080.jpg "Sensehat")

## Improvements
These are some of the improvements that I thought could be improved for the application. 

One lacking feature is the lack of **"Moon"** icons and animations. Adding more weather icons and animations for weather at night would better represent time of the day of the displayed forecast. 

The application will lag for five seconds or so whenever it is querying the OWM servers for the weather data. A Complicated improvement for this issue would be to reduce the lag of the application by making the Pi automatically query OWM servers for the weather information at regular intervals and storing this weather infomation in a database. This will allow multiple requests to the Pi without slowing the Pi down. This also reduces the risk of going over the 60-requests-per-hour limit which is set by OWM for free API keys.

This improvement is for the third function, using the joystick to display weather information. The display of the day and time could be further improved to display the exact time/date of the selection.

## Requirements
- A Raspberry Pi...
	- with the Sensehat add-on
	- and Python3 with the following modules installed
		- pyOWM
		- tzlocal

## Changelog
### v1.0
- Incomplete error checking
- Usage printing when user tries to execute with incorrect parameters
- Function to get current weather is working
- Animated weather images for displaying weather condition outputs

### v1.1
- Cleaned up error checking functions
- Prints usage when incorrect parameters are entered when running the program
- Added function to get 3-hourly forecasted weather
- Improved timezone checking functions in code (for printing time according to current timezone)

### v1.2
- Further improved error checking
- Added function to get daily forecasted weather (not working as this function requires a premium API key)
- Adjusted logic to print an animation which is closer to the current weather outside

### v1.3
- Cleaned up all bugs in error handling
- Fixed weather animation logic bug

### v1.4
- A third function to selectively display weather outputs is currently under development
- Function is incomplete, logic for changing day and time not working properly

#### v1.4.1
- Logic for changing day and time working now
- Left with output the data based on the selected time and date

#### v1.4.2
- Finished function to select weather by using joystick
- Improved smoothness by using double press to output weather instead of single press which clashes with the kill function

## References
- [OpenWeatherMap list of weather conditions](https://openweathermap.org/weather-conditions)
- [pyOWM](https://github.com/csparpa/pyowm)
- [pyOWM API documentation](http://pyowm.readthedocs.io/en/latest/_modules/pyowm/webapi25/weather.html?highlight=get_status)
- [Getting timezone](https://stackoverflow.com/questions/13218506/how-to-get-system-timezone-setting-and-pass-it-to-pytz-timezone)
- [Sensehat Guide](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat)
- [Learning the LED matrix](https://github.com/raspberrypilearning/astro-pi-guide/blob/master/inputs-outputs/led-matrix.md)
- [Sensehat API documentation](https://pythonhosted.org/sense-hat/api/#led-matrix)
- [Learning how to code with dictionaries in Python3](https://www.tutorialspoint.com/python/python_dictionary.htm)
- [Learning how to code with lists in Python3](https://www.tutorialspoint.com/python/python_lists.htm)
- [Learning about classes in Python](https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3)