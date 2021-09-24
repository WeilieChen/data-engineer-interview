"""
datelist = {
    "android": [1,0,1,0,1,0,1],
    "ios": [0,0,0,1,0,1,1],
    "web": [0,0,0,0,0,0,0]
}
metric = {
    "overall": ["ios", "android", "web"],
    "mobile": ["ios", "web"]
}

output ={
    "overall": 6
    "mobile": 3
}
"""

def total_active(datelist, metric):
    res = {}

    for k, v in metric.items():
        for n in range(7):

            active_vals = [
                d_v
                for d_k, d_v in datelist.items()
                if d_k in v
            ]
            
            tmp_max = 0
            for a_c in active_vals:
                tmp_max = max(a_c[n], tmp_max)

            res[k] = res[k] + tmp_max
    
    return res
            
