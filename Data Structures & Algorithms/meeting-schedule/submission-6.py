"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        interval = sorted(intervals,key=lambda node: node.start)
        endtime = 0
        for time in interval:
            if time.start < endtime:
                return False
            else:
                endtime = time.end
        return True
