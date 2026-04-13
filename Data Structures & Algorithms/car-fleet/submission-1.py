class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for i in range(len(position)):
            pair.append((position[i], speed[i]))

        prev_time = 0
        fleets = 0

        for p, s in sorted(pair, reverse=True):
            time = (target - p) / s
            if time > prev_time:
                fleets += 1
                prev_time = time

        return fleets