from ics import Calendar 

class calender_parser:
    def __init__(self, filename):
        self.content = self._load(filename)
        self.calendar = Calendar(self.content)
        self.events = list()

    def _load(self, filename):
        "TODO: errorchecking"
        with open(filename) as f:
            return f.read()

    def create_events(self):
        for event in self.calendar.events:
            self.events.append([event.name, event.begin.timestamp])

        self.events.sort(key=lambda val: val[1])
        for event in self.events:
            print(event)

    def get_events():
        """
        it is bad i know
        """
        if len(self.events) > 0:
            return self.events
        else:
            self.create_events()
            return self.events


if __name__ == '__main__':
    cp = calender_parser("calendar.ics")
    cp.create_events()
