"""
Given streaming event data from a log table for a multi step product, calculate the average time for each step.

+------------+------+-----------+
| session_id | step | timestamp |
+------------+------+-----------+
| 101        | 1    | 10        |
| 101        | 2    | 20        |
| 102        | 1    | 10        |
| 101        | 2    | 25        |
| 101        | 3    | 30        |
| 102        | 2    | 30        |
| 101        | 4    | 50        |
+------------+------+-----------+

The same step can appear multiple times in a single session. In this case take the earliest step's timestamp.

input = [
    [101, 1, 10],
    [101, 2, 20],
    [102, 1, 10],
    [101, 2, 25],
    [101, 3, 30],
    [102, 2, 30],
    [101, 4, 50],
]

output = {
    "1": (10 + 20) / 2
    "2": 10 / 1
    "3": 20 / 1
}
"""


step_map = {}
session_map = {}

def avg_step(session_id, step, timestamp):
    if session_id in session_map:
        if step != session_map[session_id]["prev_steps"]:
            prev_step = step - 1
            seconds_diff = timestamp - session_map[session_id]["prev_timestamp"]

            if prev_step not in step_map:
                step_map[prev_step] = {
                    "count": 1,
                    "total_sec": seconds_diff
                }
            else:
                step_map[prev_step]["count"] += 1
                step_map[prev_step]["total_sec"] += seconds_diff

            session_map[session_id]["prev_steps"] = step
            session_map[session_id]["prev_timestamp"] = timestamp
    else:
        session_map[session_id] = {"prev_steps": step, "prev_timestamp": timestamp}
    
    res = {
        k: v["total_sec"] / v["count"]
        for k, v in step_map.items()
    }

    return res

data = [
    [101, 1, 10],
    [101, 2, 20],
    [102, 1, 10],
    [101, 2, 25],
    [101, 3, 30],
    [102, 2, 30],
    [101, 4, 50],
]
for r in data:
    avg_step(*r)