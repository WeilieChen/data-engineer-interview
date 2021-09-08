"""
Your company owns a video watching platform.  Users can click to start to play the video and click stop to pause the video.  Your team is creating a real time dashboard to display the average viewing time of the users.  The data comes to you as as streaming data and includes a session_id, start_time (unix), and stop_time (unix). The viewing time would be calculated as the stop_time - start_time.  The dashboard requires the average viewing time over all time.

Write code to store and retrieve the required data efficiently. When the average viewing time is queried, it must return a result in near real time. You can assume the records will come 1 at a time and there will not be any duplicates.

Example 1:
Input = [
    {"session_id": 1, "start_time": 1626822000, "stop_time": 1626823200},
    {"session_id": 1, "start_time": 1626823500, "stop_time": 1626823800},
    {"session_id": 2, "start_time": 1626822600, "stop_time": 1626825600},
    {"session_id": 3, "start_time": 1626823800, "stop_time": 1626824700}
]
Output: 1350

The viewing time for each record is calculated as stop_time - start_time.  The average viewing time is the sum of the viewing time divided by the total number of records. The calculation should be: ((1626823200 - 1626822000) + (1626823800 - 1626823500) + (1626825600 - 1626822600) + (1626824700 - 1626823800))/4. This yields the above output.
"""

avg_dict = {"sum": 0, "count": 0}

def store(event):
    start_time = event["start_time"]
    stop_time = event["stop_time"]
    
    view_time = stop_time - start_time

    avg_dict["sum"] += view_time
    avg_dict["count"] += 1
    
def retrieve():
    avg_time = avg_dict["sum"]/avg_dict["count"]
    return avg_time

event_stream = [
    {"session_id": 1, "start_time": 1626822000, "stop_time": 1626823200},
    {"session_id": 1, "start_time": 1626823500, "stop_time": 1626823800},
    {"session_id": 2, "start_time": 1626822600, "stop_time": 1626825600},
    {"session_id": 3, "start_time": 1626823800, "stop_time": 1626824700}
]
for e in event_stream:
    store(e)

assert retrieve() == 1350
print("passed")