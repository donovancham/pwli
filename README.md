# Pi Weather LED Indicator (pwli)
This project makes use of the [Sensehat](https://www.raspberrypi.org/products/sense-hat/) add-on board for the Raspberry Pi to output open source weather data from [OpenWeatherMap](https://openweathermap.org/). This project is created using Pycharm.
 
## Abstract
 This is a project which I have undertaken while I was doing my internship at Kumamoto National College of Technology in Japan. Thanks to Kanzaki Sensei who provided me with the resources to finish the project.

## About
The project comprises of two main components, getting the weather data and displaying it. 

### Getting weather data
Getting and processing the weather data is done by using **pyOWM** which is a python API for OpenWeatherMap. However, use of this API requires an API key and the types of weather data which a free user can get is limited. As such, this application is only able to get the current weather and the 3-hourly forecast up to 5 days in advance.

### Output
For the latter, this project makes use of the Sensehats 8x8 LED matrix shown below to display the weather information. This enables the application to play animations of different weather conditions.
![8x8 Matrix](https://www.raspberrypi.org/app/uploads/2017/05/Sense-HAT-plugged-in-1-1383x1080.jpg "Sensehat")

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

## References
- [OpenWeatherMap list of weather conditions](https://openweathermap.org/weather-conditions)
- [pyOWM](https://github.com/csparpa/pyowm)
- [pyOWM API documentation](http://pyowm.readthedocs.io/en/latest/_modules/pyowm/webapi25/weather.html?highlight=get_status)
- [Getting timezone](https://stackoverflow.com/questions/13218506/how-to-get-system-timezone-setting-and-pass-it-to-pytz-timezone)
- [Sensehat Guide](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat)
- [Learning the LED matrix](https://github.com/raspberrypilearning/astro-pi-guide/blob/master/inputs-outputs/led-matrix.md)
- [Sensehat API documentation](https://pythonhosted.org/sense-hat/api/#led-matrix)