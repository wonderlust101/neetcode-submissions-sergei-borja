class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) # [timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        value = ""

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][0] <= timestamp:
                value = values[m][1]
                l = m + 1
            else:
                r = m - 1
            

        return value

