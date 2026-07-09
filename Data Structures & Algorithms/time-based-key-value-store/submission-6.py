class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = {timestamp: value}
            self.keys[key]["timestamps"] = [timestamp]
        else:
            self.keys[key][timestamp] = value
            self.keys[key]["timestamps"].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys or len(self.keys[key]["timestamps"]) == 0:
            return ""
        if timestamp in self.keys[key]:
            return self.keys[key][timestamp]
        n = len(self.keys[key]["timestamps"])
        last = self.keys[key]["timestamps"][-1]
        if last < timestamp:
            return self.keys[key][last]
        if self.keys[key]["timestamps"][0] > timestamp:
            return ""
        left = 0
        right = n - 1
        while left <= right:
            mid = (right + left) // 2
            if self.keys[key]["timestamps"][mid] < timestamp and self.keys[key]["timestamps"][mid+1] > timestamp:
                return self.keys[key][self.keys[key]["timestamps"][mid]]
            elif self.keys[key]["timestamps"][mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        return ""