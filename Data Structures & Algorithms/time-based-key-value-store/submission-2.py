class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = {timestamp: value}
        self.keys[key][timestamp] = value
        print(self.keys)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        while timestamp not in self.keys[key]:
            timestamp -= 1
            if timestamp < 0:
                return ""
        return self.keys[key][timestamp]
