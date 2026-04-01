import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            d = (p[0]**2 + p[1]**2)**0.5
            distances.append([d, p])
        heapq.heapify(distances)

        kclose = []

        for i in range(k):
            p = heapq.heappop(distances)
            kclose.append(p[1])

        return kclose