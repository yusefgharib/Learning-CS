class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @classmethod
    def from_string(cls, string):
        hour = (string.split(':')[0])
        minute = (string.split(':')[1])
        return cls(hour, minute)
