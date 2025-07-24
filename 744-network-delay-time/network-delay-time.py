from collections import defaultdict, deque
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = defaultdict(list) # node: [(dest, time)]
        for node, dest, time in times:
            nodes[node].append((dest, time))

        # bfs start in k
        minHeap = [ (0, k) ] # (curTime, index)
        heapq.heapify(minHeap) 
        visited = set() # indexes
        maxTime = float('-inf')

        while minHeap:
            curTime, index = heapq.heappop(minHeap)

            if index in visited:
                continue
                
            visited.add(index)
            maxTime = max(maxTime, curTime)

            for dest, time in nodes[index]:
                heapq.heappush(minHeap, (curTime + time, dest))
                    
        return maxTime if len(visited) == n else -1
