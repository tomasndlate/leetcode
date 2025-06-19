from collections import defaultdict, deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        alive = defaultdict(int)
        queue = deque()
        for s in senate:
            alive[s] += 1
            queue.append(s)
        
        opposite = { "R":"D", "D":"R" }
        ban = defaultdict(int)
        
        while alive["R"] and alive["D"]:
            senator = queue.popleft()

            if ban[senator]:
                ban[senator] -= 1
                alive[senator] -= 1
            else:
                ban[opposite[senator]] += 1
                queue.append(senator)


        mapping = { "R": "Radiant", "D": "Dire" }
        return mapping[queue[0]]