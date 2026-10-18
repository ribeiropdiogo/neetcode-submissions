class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        else:
            l, r = 0, len(self.map[key])-1
            maxt = float('-inf')
            res = ""
            while l <= r:
                m = (l+r)//2
                t, v = self.map[key][m]
                if t > maxt and t <= timestamp:
                    maxt = t
                    res = v
                if t > timestamp:
                    r = m - 1
                else:
                    l = m + 1
        return res




        
