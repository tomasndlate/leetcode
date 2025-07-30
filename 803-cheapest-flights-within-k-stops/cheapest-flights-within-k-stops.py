from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list) # src: [(cost, dest)]

        for source, dest, cost in flights:
            graph[source].append((cost, dest))
        #print(graph)
        minHeap = [(0, src, 0)] # cost, source, stops
        visited = {} # (stops, source): cur_cost
        while minHeap:
            cost, source, stops = heapq.heappop(minHeap)
            #print('cost', cost, 'source', source, 'stops', stops)
            if source == dst:
                return cost
            if stops > k:
                continue

            for price, dest in graph[source]:
                if (stops + 1, dest) not in visited or cost + price < visited[(stops + 1, dest)]:
                    visited[(stops + 1, dest)] = cost + price
                    heapq.heappush(minHeap, (cost + price, dest, stops + 1))

        return -1
