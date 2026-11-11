class TimeMap:

    def __init__(self):
        self.data = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.data:
            return self.data[key, timestamp]
        else:
            while timestamp>=1:
                timestamp-=1
                if (key, timestamp) in self.data:
                    return self.data[key, timestamp]
            return ""

