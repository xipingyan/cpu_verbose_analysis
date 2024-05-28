# Statistic all oneDNN consume time.

import numpy as np

fn="ipex_onednn_verbose.txt"
# fn="ov_onednn_verbose.txt"

f = open(fn, "r", errors='replace')
lines = f.readlines()
# f.close()

all_time = 0
reorder_tm = 0
for line in lines:
    ss = line.split(",")
    try:
        tm = float(ss[-1])
    except:
        print(f"Error: {ss[-1]} can't convert to float.")
        continue
    all_time = all_time + tm
    if line.find("cpu,reorder,") >= 0:
        reorder_tm = reorder_tm + tm

print(f"final result: all_time={all_time}, reorder_tm={reorder_tm}, reorder_tm/all_time={reorder_tm*100/all_time}%")
