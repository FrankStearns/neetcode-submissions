import bisect

class TimeMap:

    def __init__(self):
        self.values = {}
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = {}
            self.timestamps[key] = []
        
        self.values[key][timestamp] = value
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""

        if timestamp in self.values[key]:
            return self.values[key][timestamp]
            
        time_list = self.timestamps[key]
        
        if not time_list or time_list[0] > timestamp:
            return ""
        if time_list[-1] < timestamp:
            return self.values[key][time_list[-1]]
            
        idx = bisect.bisect_right(time_list, timestamp)
        
        actual_timestamp = time_list[idx - 1]
        return self.values[key][actual_timestamp]