class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Why do I need a stack when I can just do without stack
        count = 0
        pair = []
        for i in range(len(position)):
            pair.append((position[i], speed[i]))

        prev_time = 0
        for p, s in sorted(pair)[::-1]:
            dist = target - p
            time = dist / s
            if prev_time == 0:
                prev_time = time
            else:
                if time > prev_time:
                    count += 1
                    prev_time = time

        return count + 1