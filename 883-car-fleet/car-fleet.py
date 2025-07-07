class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target = (speed * time) + position <=> time = (target - position) / speed
        cars = [ (p, (target - p) / s) for p, s in zip(position, speed) ] # (position, time)
        cars.sort(key=lambda x: x[0], reverse=True)
        
        time = 1
        fleets = [cars[0][time]] # initiate with first car time to reach

        for car in cars[1:]:
            # if time to reach higher than fleet, new fleet, else nothing happen
            if car[time] > fleets[-1]:
                fleets.append(car[time])
        
        return len(fleets)