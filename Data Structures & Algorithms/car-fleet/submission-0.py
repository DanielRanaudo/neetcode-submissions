class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        fleets = 0
        max_time = float('-inf')
        for i in range(len(position) - 1, -1, -1):
            pos, s = cars[i]
            time = (target - pos) / s
            if time > max_time:
                fleets += 1
                max_time = time

        return fleets
        