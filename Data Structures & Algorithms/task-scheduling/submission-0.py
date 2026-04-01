import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_d = {}
        for i in tasks:
            task_d[i] = task_d.get(i, 0) + 1
        task_heap = []

        heapq.heapify(task_heap)
        for k, v in task_d.items():
            task_heap.append([-1 * v, k])

        print(task_heap)

        running = deque()
        run_seq = []
        while task_heap:
            t = heapq.heappop(task_heap)
            no = True
            for run in running:
                if t[1] == run[0][1]:
                    no = False
            if no:
                run_seq.append(t[1])
                t[0] += 1
                
                for i in running:
                    i[1] += 1

                if t[0] != 0:
                    running.append([t, 0])
                if running and running[0][1] == n:
                    t1 = running.popleft()
                    heapq.heappush(task_heap, t1[0])

            if not task_heap and running:
                while running and running[0][1] != n:
                    run_seq.append("idle")
                    for i in running:
                        i[1] += 1
                t2 = running.popleft()
                heapq.heappush(task_heap, t2[0])

        return len(run_seq)