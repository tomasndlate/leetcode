from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasksCount = Counter(tasks)

        queue = deque()             # availability (blockUntil, remainingTask)
        heap = [ -count for count in tasksCount.values() ]  # priority
        heapq.heapify(heap)

        time = 0
        while heap or queue:
            time += 1
            
            while queue and queue[0][0] < time:
                blockUntil, task = queue.popleft()
                heapq.heappush(heap, -task)
            
            if heap:
                task = -heapq.heappop(heap)
                task -= 1

                if task > 0: # still need to process
                    queue.append((time + n, task))
        
        return time