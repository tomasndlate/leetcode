class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g - c for g, c in zip(gas, cost)]
        
        if sum(diff) < 0: # impossible
            return -1
        
        accumulated = 0
        index = 0

        for i, fuel in enumerate(diff):
            accumulated += fuel
            if accumulated < 0: # don't reach next
                accumulated = 0
                index = i + 1
        
        return index

