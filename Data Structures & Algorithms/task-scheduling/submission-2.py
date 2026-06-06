from _heapq import heappop
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        heap = [-val for val in freq.values()]

        heapq.heapify(heap)

        time = 0

        while heap:
            tmp = []
            cycle=n+1


            while heap and cycle > 0:
                count = heapq.heappop(heap)
                count += 1

                if count < 0:
                    tmp.append(count)
                
                time +=1
                cycle -= 1

            for count in tmp:
                heapq.heappush(heap, count)

            if heap:
                time += cycle

        return time

