#!/usr/bin/env python
import psutil
from datetime import datetime
from os import path
import os

# Monitoring software developed by Crhistian Segura on 2021 import psutil

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")
timestamp = dateTimeObj.strftime("%d-%b-%Y_%H:%M:%S")
#print('Current Timestamp : ', timestampStr)

path_logs="/home/cubo/monitor_logs"
if(not path.exists(path_logs)):
        os.mkdir(path_logs)
fileName=f"{path_logs}/data_{timestampStr}.csv"

mem = psutil.virtual_memory().percent
cpu_usage = psutil.cpu_percent(interval=0.1, percpu=True)

cpu_cores = len(cpu_usage)

stats_root = psutil.disk_usage('/')
stats_dc = psutil.disk_usage('/dc_storage')
stats_web = psutil.disk_usage('/web_storage')
stats_source = psutil.disk_usage('/source_storage')

if(path.exists(fileName)):
    #print('append')
    with open(fileName, "a") as myfile:
        myfile.write(f"{mem};")
        for i in range(cpu_cores):
            myfile.write(f"{cpu_usage[i]};")
        myfile.write(f"{stats_root.percent};")
        myfile.write(f"{stats_dc.percent};")
        myfile.write(f"{stats_web.percent};")
        myfile.write(f"{stats_source.percent};")
        myfile.write(f"{timestamp}\n")
else:
    # create
    with open(fileName, "w") as myfile:
        myfile.write("memory;")
        for i in range(cpu_cores):
            myfile.write(f"core {i};")
        myfile.write("root /;")
        myfile.write("dc_storage;")
        myfile.write("web_storage;")
        myfile.write("source_storage;")
        myfile.write("time_stamp")
        myfile.write("\n")
