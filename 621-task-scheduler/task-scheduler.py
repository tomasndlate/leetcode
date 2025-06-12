from collections import defaultdict, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasksCount = Counter(tasks)
        heap = [ -freq for freq in tasksCount.values() ]
        heapq.heapify(heap)
        queue = collections.deque() # (numTasks, availableAt)

        time = 0
        while heap or queue:
            if queue and time > queue[0][1]:
                numTask = queue.popleft()[0]
                heapq.heappush(heap, -numTask)
            
            if heap:
                numTask = (-heapq.heappop(heap)) - 1
                if numTask > 0:
                    queue.append((numTask, time + n))
            
            time += 1
        
        return time