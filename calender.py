from ics import Calendar
import requests
import time
import re

class calender_parser:
    def __init__(self, url):
        self.content = requests.get(url).text 
        self.calendar = Calendar(self.content)
        self.events = list()

    def create_events(self, filter_desc = []):
        """
        TODO: Errorchecking
        """
        for event in self.calendar.events:
            if re.search(r'Forelesning', event.description, re.M|re.I) or re.search(r'Lecture', event.description, re.M|re.I):
                self.events.append([event.name, event.begin.timestamp, event.description, True])
            else:
                self.events.append([event.name, event.begin.timestamp, event.description, False])
        self.events.sort(key=lambda val: val[1])
        # for event in self.events:
        #     if event[3]:
        #         print(event)
        # print(len(self.events))

    def get_events(self):
        """
        it is bad i know
        """
        if len(self.events) > 0:
            return self.events
        else:
            self.create_events()
            return self.events

    def get_next_lecture(self, lim = 60*60*24*7):
        time_now = int(time.time())
        upcoming_events = list()
        for event in self.events:
            if event[1] - time_now > 0 and event[1] - time_now < lim and event[3]:
                upcoming_events.append(event)
        print(upcoming_events)



if __name__ == '__main__':
    courses = ["INF-2900-1", "INF-2310-1", "INF-1400-1", "MAT-2300-1", "MAT-1002-1", "FIL-0700-1", "BED-2017-1"]
    url = "https://timeplan.uit.no/calendar.ics?sem=21v"
    for course in courses:
        url += f"&module[]={course}"
    cp = calender_parser(url)
    cp.create_events(["Lectures", "Forelesning (opptak med direktesending)  &nbsp;Opptak", "Forelesninger  &nbsp;Opptak"])
    cp.get_next_lecture()
