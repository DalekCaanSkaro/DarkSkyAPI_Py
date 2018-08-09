import requests
import json
import datetime
import time

class HourInfo(object):

    def __init__(self, Hr):
        self.Hr = Hr

    def HourNo(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        
        sixtyCount = 0
        now = time.strftime("%H", time.localtime(time.time()))
        t0 = time.time()
        if self.Hr==0:
            hr_curr = "Currently"
            return print(hr_curr)
        else:
            sixtyCount = sixtyCount + (60 * self.Hr)
            t1 = t0 + 60*sixtyCount
            hr_curr = time.strftime("%I%p",time.localtime(t1))
            return print(hr_curr)

    def HourSummary(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        return print(results["hourly"]["data"][self.Hr]["summary"])

    def HourPrecipProb(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        return print(results["hourly"]["data"][self.Hr]["precipProbability"])

    def HourPrecipType(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        try:
            return print(results["hourly"]["data"][self.Hr]["precipType"])
        except:
            return print("No Precipitation")
    
    def HourTemp(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        return print(results["hourly"]["data"][self.Hr]["temperature"])
        
    def HourHumidity(self):
        with open('JSON_Test.json') as f:
            results = json.load(f)
        return print(results["hourly"]["data"][self.Hr]["humidity"])