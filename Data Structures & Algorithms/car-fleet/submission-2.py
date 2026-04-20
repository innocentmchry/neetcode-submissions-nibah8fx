class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0
        
        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])

        pair.sort()
        fleet = 1
        dist = target - pair[len(pair)-1][0]
        prev_time = dist / pair[len(pair)-1][1]
        for i in range(len(position) - 2, -1, -1):
            pos, speed = pair[i]
            dist = target - pos
            time = dist / speed
            if time > prev_time:
                prev_time = time
                fleet += 1

        return fleet