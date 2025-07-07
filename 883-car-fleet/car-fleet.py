class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0

        # target = (speed * time) + position <=> time = (target - position) / speed
        cars = [ (p, (target - p) / s) for p, s in zip(position, speed) ] # (position, time)
        cars.sort(key=lambda x: x[0], reverse=True)
        
        fleets = 0
        fleet_time = 0.0 # initiate with first car time to reach

        for _, time in cars:
            # if time to reach higher than fleet, new fleet
            if time > fleet_time:
                fleet_time = time
                fleets += 1
        
        return fleets