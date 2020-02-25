from datetime import datetime
import re

def start():
    now = datetime.now()
    start_time = now.strftime("%H:%M:%S")
    start_time_list = re.split(":", start_time)
    return start_time_list


def elapsed_time():
    stop_time = now.strftime("%H:%M:%S")
    stop_time_list = re.split(":", stop_time)
    time_elapsed = (int(stop_time_list[0]) - int(start_time_list[0]) * 60) + (
            int(stop_time_list[1]) - int(start_time_list[1])) + (
                           int(stop_time_list[2]) - int(start_time_list[2])) // 60
    return time_elapsed
