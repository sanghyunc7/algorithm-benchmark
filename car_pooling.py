import heapq


class Solution:
    def carPooling(self, trips, capacity) -> bool:
        # max overlapping intervals should be less than capacity
        # sort by starting interval
        # insert in min-heap by finishing time
        trips.sort(key=lambda x: x[1])
        passengers = 0
        hp = []
        for t in trips:
            while hp and t[1] >= hp[0][0]:
                passengers -= heapq.heappop(hp)[1]
            heapq.heappush(hp, (t[2], t[0]))
            passengers += t[0]
            if passengers > capacity:
                return False
        return True
