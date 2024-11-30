class Event:
    def __init__(self, name, date, status):
        self.name = name
        self.date = date
        self.status = status

    def __str__(self):
        return f"Event Name: {self.name}, Date: {self.date}, Status: {self.status}"
