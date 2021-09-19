"""
920. https://www.lintcode.com/problem/920/description

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

(0,8),(8,10) is not conflict at 8

Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict

Example2
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        if len(intervals) == 0:
            return True

        intervals = [(i.start, i.end) for i in intervals]
        intervals = sorted(intervals)

        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]

            if prev[1] > cur[0]:
                return False

        return True

    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key=lambda x: x.start)
        maxend = -1
        for i in intervals:
            if i.start < maxend:
                return False
            maxend = max(maxend, i.end)
        return True