class MedianFinder:
    # INSERT in order solution

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        i = 0
        while i < len(self.arr):
            if num < self.arr[i]:
                temp = self.arr[i: len(self.arr)]
                self.arr[i] = num
                self.arr = self.arr[:i+1] + temp
                return None

            i += 1
    
        if i == len(self.arr):
            self.arr.append(num)
        return None

    def findMedian(self) -> float:
        if len(self.arr) == 0:
            return 0.0

        if len(self.arr) % 2 == 1:
            median_idx = (len(self.arr) - 1) // 2
            return float(self.arr[median_idx])
        else:
            median_idx1 = (len(self.arr) - 1) // 2
            return (self.arr[median_idx1] + self.arr[median_idx1 + 1]) / 2 
        
        