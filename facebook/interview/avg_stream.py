
"""
step_map = {
    1: {
        "session_count": 2
        "total_sec": 20
    }
}
"""
step_map = {}
"""
sesssion_map = {
    10: {
        "seen_steps": (1, 2)
        "prev_timestamp": 20200101
    }
}
"""
session_map = {}

def avg_step(session_id, step, timestamp):
    if session_id in session_map:
        if step not in session_map[session_id]["seen_steps"]:
            total = timestamp - session_map[session_id]["prev_timestamp"]

            step_map[step]["total_sec"] += total
            step_map[step]["count"] += 1

            session_map[session_id]["seen_steps"] = session_map[session_id]["seen_steps"].add(step)
            session_map[session_id]["prev_timestamp"] = timestamp

    else:
        session_map[session_id][step] = timestamp
        step_map[step]["count"] += 1
    
    return {
        k: v["total_sec"] / v["session_count"]
        for k, v in step_map.items()
    }
