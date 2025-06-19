from collections import defaultdict, deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = defaultdict(int)
        queue = deque()
        for s in senate:
            count[s] += 1
            queue.append(s)
        
        opposite = { "R":"D", "D":"R" }
        exclude = defaultdict(int)
        
        while count["R"] and count["D"]:
            cur = queue.popleft()

            if exclude[cur]:
                exclude[cur] -= 1
                count[cur] -= 1
            else:
                exclude[opposite[cur]] += 1
                queue.append(cur)


        mapping = { "R": "Radiant", "D": "Dire" }
        return mapping[queue[0]]