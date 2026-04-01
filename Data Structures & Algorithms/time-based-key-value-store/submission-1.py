class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key] = self.timemap.get(key, [])
        self.timemap[key].append([value, timestamp])
        print(self.timemap)
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap.keys():
            return ""
        arr = self.timemap[key]
        l = 0
        r = len(arr) - 1
        timestamp_le = -1
        timemap_index = -1

        while l <= r:
            mid = (l + r)//2

            if arr[mid][1] == timestamp:
                return arr[mid][0]
            
            elif arr[mid][1] < timestamp:
                timestamp_le = max(timestamp_le, arr[mid][1])
                timemap_index = mid
                l = mid + 1
            
            else:
                r = mid - 1
        
        if timemap_index != -1:
            return arr[timemap_index][0]
        return ""