"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in intervals:
            for j in intervals:
                if i == j:
                    continue
                if (i.end > j.start and i.start < j.end):
                    return False
                    
        return True 