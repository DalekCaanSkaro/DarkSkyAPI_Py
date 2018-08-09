import requests
import json
import datetime
import time
#import urllib
#import geopy

class DailyInfo(object):

    def __init__(self, day):
        self.day = day

    def DailySummary(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        return print(results["daily"]["data"][self.day]["summary"])
    
    def DailyPecipProb(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        return print(results["daily"]["data"][self.day]["precipProbability"])
    
    def DailyPrecipType(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        try:
            print(results["daily"]["data"][self.day]["precipType"])
        except:
            print("No Precipitation")
    
    def DailyTempHigh(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        return print(results["daily"]["data"][self.day]["apparentTemperatureHigh"])
    
    def DailyTempLow(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        return print(results["daily"]["data"][self.day]["apparentTemperatureLow"])
    
    def DailyIcon(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        print(results["daily"]["data"][self.day]["icon"])