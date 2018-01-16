#!/usr/bin/python3.4
import pyowm
from pyowm.caches.lrucache import LRUCache
from tzlocal import get_localzone

cache = LRUCache()

owm = pyowm.OWM('17e4ce9b0c933a0ba624231ebbc3afe8')
reg = owm.city_id_registry()

# Multiple Output:
# If Fail: True
# If Success: False, status
def getcweather(location):
    # Code to clean up location search results
    searchloc = reg.ids_for(location, matching='like')
    if len(searchloc) == 0:
        return False
    cleanloc = searchloc[0]
    location = cleanloc[1]

    # Get weather observation of the location
    obs = owm.weather_at_place(location)

    # Get timestamp of when data is retrieved
    dt = obs.get_reception_time(timeformat='date')
    timezone = get_localzone()
    localtime = dt.astimezone(timezone)
    time = localtime.strftime("%A, %-d %B %Y %-I:%M%p")

    # Code to get location data
    l = obs.get_location()
    location = l.get_name()

    # The code to get Weather object from obs
    w = obs.get_weather()
    temp = w.get_temperature(unit='celsius')
    current = w.get_detailed_status()
    code = w.get_weather_code()

    # DEBUG
    print(location, time, "weather ID: " + str(code), "Current Weather: " + current, "Temp: " + str(temp['temp']), sep='\n')
    return True, code, temp['temp']

# Get forecast weather for 3-hourly intervals based on location, date and time of the requested forecast
def get3hfweather(location, dayslater, stime):
    # Code to clean up location search results
    searchloc = reg.ids_for(location, matching='like')
    if len(searchloc) == 0:
        return False
    cleanloc = searchloc[0]
    location = cleanloc[1]

    # Get forecast object
    fc = owm.three_hours_forecast(location)
    f = fc.get_forecast()

    # Get timestamp of when data is retrieved
    dt = f.get_reception_time('date')
    timezone = get_localzone()
    localtime = dt.astimezone(timezone)
    time = localtime.strftime("%A, %-d %B %Y %-I:%M%p")
    first_day = localtime.strftime("%-d")

    laterd = int(first_day) + int(dayslater)

    output = {'Location': location, 'Current Time': time}

    for fweather in f:
        # Get time of forecast
        ftime = fweather.get_reference_time('date')
        flocaltime = ftime.astimezone(timezone)
        checkt = flocaltime.strftime("%-H")
        checkd = flocaltime.strftime("%-d")
        if int(checkd) == int(laterd):
            if int(checkt) == int(stime):
                time = flocaltime.strftime("%A, %-I:%M%p")
                current_day = flocaltime.strftime("%m/%d")

                # Get output to return
                wcode = fweather.get_weather_code()
                cond = fweather.get_status()
                temp = fweather.get_temperature(unit='celsius')['temp']

                print(output, current_day, time, wcode, cond, temp, sep='\n')

                return True, wcode, temp

    return False

def getfullfweather(location):
    # Day checker
    setofdays = set()

    # Code to clean up location search results
    searchloc = reg.ids_for(location, matching='like')
    if len(searchloc) == 0:
        return False
    cleanloc = searchloc[0]
    location = cleanloc[1]

    # Get forecast object
    fc = owm.three_hours_forecast(location)
    f = fc.get_forecast()

    # Get timestamp of when data is retrieved
    dt = f.get_reception_time('date')
    timezone = get_localzone()
    localtime = dt.astimezone(timezone)
    time = localtime.strftime("%A, %-d %B %Y %-I:%M%p")

    print(location, time, "\n", sep='\t')

    output = {}

    for fweather in f:
        # Get time of forecast
        ftime = fweather.get_reference_time('date')
        flocaltime = ftime.astimezone(timezone)
        time3 = flocaltime.strftime("%-H")
        current_day = flocaltime.strftime("%-m/%-d")

        # Get condition
        wcode = fweather.get_weather_code()
        #Get temperature
        temp = fweather.get_temperature(unit='celsius')['temp']

        if current_day not in output:
            output.update({current_day: {}})
            if time3 not in output[current_day]:
                output[current_day].update({time3: {}})
        else:
            if time3 not in output[current_day]:
                output[current_day].update({time3: {}})

        data = {"ID": wcode, "Temperature": temp}
        output[current_day][time3].update(data)

    return True, output

# # Get forecast weather for the day based on location and day
# def getdailyfweather(location, dayslater):
#     # Code to clean up location search results
#     searchloc = reg.ids_for(location, matching='like')
#     if len(searchloc) == 0:
#         return False
#     cleanloc = searchloc[0]
#     location = cleanloc[1]
#
#     # Get forecast object
#     fc = owm.daily_forecast(location)
#     f = fc.get_forecast()
#
#     # Get timestamp of when data is retrieved
#     dt = f.get_reception_time('date')
#     timezone = get_localzone()
#     localtime = dt.astimezone(timezone)
#     time = localtime.strftime("%A, %-d %B %Y %-I:%M%p")
#     first_day = localtime.strftime("%-d")
#
#     laterd = int(first_day) + int(dayslater)
#
#     output = {'Location': location, 'Current Time': time}
#
#     for fweather in f:
#         # Get time of forecast
#         ftime = fweather.get_reference_time('date')
#         flocaltime = ftime.astimezone(timezone)
#         checkd = flocaltime.strftime("%-d")
#         if int(checkd) == int(laterd):
#             time = flocaltime.strftime("%A, %-I:%M%p")
#             current_day = flocaltime.strftime("%m/%d")
#
#             # Get output to return
#             code = fweather.get_weather_code()
#             cond = fweather.get_status()
#             temp = fweather.get_temperature(unit='celsius')['temp']
#
#             print(output, current_day, time, code, cond, temp, sep='\n')
#
#             return True, code, temp
#
#     return False