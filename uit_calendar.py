from ics import Calendar
import requests
import time
import re

class Event:
    def __init__(self, name, timestamp, desc, lecture):
        self.name = name
        self.timestamp = timestamp
        self.desc = desc
        self.lecture = lecture

    def __str__(self):
        return f"{self.name}, {time.ctime(self.timestamp)}, {self.desc}, {self.lecture}"

class Calendar_parser:
    def __init__(self, url):
        self.content = requests.get(url).text
        self.calendar = Calendar(self.content)
        self.events = list()

    def create_events(self):
        for event in self.calendar.events:
            if re.search(r'Forelesning', event.description, re.M|re.I) or re.search(r'Lecture', event.description, re.M|re.I):
                self.events.append(Event(event.name, event.begin.timestamp, event.description, True))
            else:
                self.events.append(Event(event.name, event.begin.timestamp, event.description, False))
        self.events.sort(key=lambda e: e.timestamp)

    def print_events(self):
        for event in self.events:
            print(event)

    def get_next_lecture(self, lim = 60*15):
        time_now = int(time.time())
        upcoming_events = list()
        for event in self.events:
            if event.timestamp - time_now > 0 and event.timestamp - time_now <= lim and event.lecture:
                upcoming_events.append(event)
            if event.timestamp - time_now > lim:
                break
        for event in upcoming_events:
            print(event)
        return upcoming_events


if __name__ == '__main__':
    courses = ["INF-2900-1", "INF-2310-1", "INF-1400-1", "MAT-2300-1", "MAT-1002-1", "FIL-0700-1", "BED-2017-1"]
    url = "https://timeplan.uit.no/calendar.ics?sem=21v"
    for course in courses:
        url += f"&module[]={course}"
    cp = Calendar_parser(url)
    cp.create_events()
    cp.get_next_lecture(60*60*24*3)