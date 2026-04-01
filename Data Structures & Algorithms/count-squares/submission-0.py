class CountSquares:

    def __init__(self):
        self.ptscount = defaultdict(int)
        self.ptslist = []

    def add(self, point: List[int]) -> None:
        self.ptslist.append(point)
        self.ptscount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.ptslist:
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            res += self.ptscount[(x, py)] * self.ptscount[(px, y)]
        return res