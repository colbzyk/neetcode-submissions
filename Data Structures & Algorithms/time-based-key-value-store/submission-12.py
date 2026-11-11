class TimeMap:

    def __init__(self):
        self.data = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.data:
            return ""
        values = self.data[key]

        l, r = 0, len(values)-1
        res = ""

        while l<=r:
            m = (l+r) // 2

            if timestamp >= values[m][1]:
                l = m + 1
                res = values[m][0]
            else:
                r = m - 1

        return res
            
            
            

