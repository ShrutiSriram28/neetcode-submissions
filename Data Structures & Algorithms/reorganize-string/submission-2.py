class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        pq = []
        heapq.heapify(pq)

        for c in s:
            count[c] = count.get(c, 0) + 1

        for k, v in count.items():
            heapq.heappush(pq, [-v, k])

        check = heapq.heappop(pq)

        if -1 * check[0] > (len(s) + 1)//2:
            print(-1 * check[0], (len(s) + 1)//2)
            return ""

        heapq.heappush(pq, check)

        s1 = ""

        track = [1, ""]
        while pq:
            c = heapq.heappop(pq)
            s1 += c[1]
            c[0] += 1

            if track[0] < 0:
                heapq.heappush(pq, track)
            track = c
            
            print(s1)

        return s1