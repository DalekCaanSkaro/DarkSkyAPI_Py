import requests
import json
import urllib
import geopy
from geopy.geocoders import GoogleV3
import Hourly
import Daily

url = "https://api.darksky.net/forecast/<Add Web Key Here>/39.9522222,-75.1641667"
# geopy.geocoders.options.default_timeout = 15
# geolocator = GoogleV3(api='AIzaSyAgfhSYbSFa83gb9aMiExI6hksxeQ-VwKo',format_string="%s, New York City, NY")
# print(str(geolocator.geocode("175 5th Avenue")))

# location = geolocator.geocode("New York City, NY")
# data = "latitude: 37.8267, longitude: -122.4233"

# print(location.address)

response = requests.get(url) #, data=data)

# rspDict = json.loads(response)

# rspDict[latitude]

# myList = str(response.json()).split("':")

# print(response.json())
# print("\n")
# print(myList) 

myList = response.json()

parsed = json.dumps(myList, sort_keys=True, indent=4, separators=(',', ': '))

# print(json.dumps(myList, sort_keys=True, indent=4, separators=(',', ': ')))

print('\n')

text_file = open("JSON_Test.json", "w")
text_file.write(str(json.dumps(myList, sort_keys=True, indent=4, separators=(',', ': '))))

text_file.close()

print('\n')

with open('JSON_Test.json') as f:
    data = json.load(f)

#print(data["hourly"]["data"][0]["summary"])
'''
print(data["hourly"]["data"][0]["summary"])
print(data["hourly"]["data"][0]["precipProbability"])
print(data["hourly"]["data"][0]["precipType"])
print(data["hourly"]["data"][0]["temperature"])
print(data["hourly"]["data"][0]["humidity"])
'''
# HourSummary = Hourly.HourInfo(0).HourSummary
# The_Daily = Daily.DailyInfo(0)

curr_apptTemp = data["currently"]["apparentTemperature"]
curr_humidity = data["currently"]["humidity"]
curr_icon = data["currently"]["icon"]
curr_precipProb = data["currently"]["precipProbability"]
curr_temp = data["currently"]["temperature"]
print("\n")

print(curr_apptTemp)
print(curr_humidity)
print(curr_icon)
print(curr_precipProb)
print(curr_temp)

print("\n")

Hourly.HourInfo(0).HourNo()
Hourly.HourInfo(0).HourSummary()
Hourly.HourInfo(0).HourPrecipProb()
Hourly.HourInfo(0).HourTemp()
Hourly.HourInfo(0).HourHumidity()

Daily.DailyInfo(0).DailySummary()
Daily.DailyInfo(0).DailyPecipProb()
Daily.DailyInfo(0).DailyPrecipType()
Daily.DailyInfo(0).DailyTempHigh()
Daily.DailyInfo(0).DailyTempLow()

# print(data["timezone"])

'''
print(data["timezone"])
print(data["alerts"][0]["expires"])
# This does not work print(data["daily"][0]["data"])
print(data["daily"]["data"][0]["apparentTemperatureHigh"])
print(data["daily"]["data"][1]["apparentTemperatureHigh"])
'''

#with open("JSON_Test.json") as json_file:
#    json_data = json.load(json_file)
#    print(json_data)
