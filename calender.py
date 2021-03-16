from datetime import datetime
from stringcolor import * 
import os 

date = datetime.now()
todaysDay = date.day()
todaysMonth = date.month()
todaysYear = date.year()

class event:
    def __init__(self, isRecurring, day, month, year, time, eventName) -> None:
        self.isRecurring = isRecurring 
        self.day = day
        self.month = month 
        self.year = year
        self.time = time 
        self.eventName = eventName

    def isToday(self) -> bool:
        global todaysYear
        global todaysMonth 
        global todaysDay
        return True if self.year == todaysYear and self.month == todaysMonth and self.day == todaysDay else False


class events:
    def __init__(self) -> None:
        self.data = {}

    def addEvent(self, eventData: event) -> None:
        if not eventData.year:
            global todaysYear
            eventData.year = todaysYear
        if eventData.year not in self.data.keys():
            self.data[eventData.year] = {}
        if eventData.month not in self.data[eventData.year].keys():
            self.data[eventData.year][eventData.month] = {}
        if eventData.day not in  self.data[eventData.year][eventData.month].keys():
             self.data[eventData.year][eventData.month][eventData.day] = [eventData]

        if eventData.isToday():
            if "Today" in self.data.keys():
                self.data["Today"].append(eventData)
            else:
                self.data["Today"] = [eventData]

    def todaysEvents(self) -> None:
        if "Today" in self.data.keys():
            print(cs("Todays Events","purple4"))
            for event in self.data

 