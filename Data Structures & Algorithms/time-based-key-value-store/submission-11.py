class TimeMap:

    def __init__(self):
        self.data = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            values = self.data[key] #["happy", 1], ...
        else:
            return ""
        
        if len(values) == 0:
            return ""
        l, r = 0, len(values)-1
        res = values[r][1]
        rightMost = ""

        while l<=r:
            m = (l+r) // 2

            if timestamp >= values[m][1]:
                l = m + 1
                rightMost = values[m][0]
            elif timestamp < values[m][1]:
                r = m - 1
            elif timestamp == values[m][1]:
                return values[m][0]
        return rightMost
            
            
            

