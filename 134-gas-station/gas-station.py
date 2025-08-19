class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Impossible, at some point no fuel
        if sum(g - c for g, c in zip(gas, cost)) < 0:
            return -1

        fuel = 0
        index = 0

        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                fuel = 0
                index = i + 1
        
        return index
