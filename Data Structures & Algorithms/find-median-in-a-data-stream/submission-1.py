class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        return None

    def findMedian(self) -> float:
        if len(self.arr) == 0:
            return 0.0

        self.arr.sort()
        if len(self.arr) % 2 == 1:
            median_idx = (len(self.arr) - 1) // 2
            return float(self.arr[median_idx])
        else:
            median_idx1 = (len(self.arr) - 1) // 2
            return (self.arr[median_idx1] + self.arr[median_idx1 + 1]) / 2 