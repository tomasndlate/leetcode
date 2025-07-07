class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0

        # target = (speed * time) + position <=> time = (target - position) / speed
        cars = [ (p, (target - p) / s) for p, s in zip(position, speed) ] # (position, time)
        cars.sort(key=lambda x: x[0], reverse=True)
        
        TIME_IDX = 1
        fleets = 1
        fleet_time = cars[0][TIME_IDX] # initiate with first car time to reach

        for car in cars[1:]:
            # if time to reach higher than fleet, new fleet
            if car[TIME_IDX] > fleet_time:
                fleet_time = car[TIME_IDX]
                fleets += 1
        
        return fleets