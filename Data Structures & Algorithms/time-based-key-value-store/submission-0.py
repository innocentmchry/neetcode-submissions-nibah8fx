class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.hashmap:
            arr = self.hashmap[key]
            l, r = 0, len(arr) - 1
            
            while l <= r:
                mid = (l + r) // 2

                if arr[mid][0] <= timestamp >= arr[mid][0]:
                    res = arr[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
        
        return res

