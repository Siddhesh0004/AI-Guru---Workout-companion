from datetime import datetime

seconds = 0
minutes = 0
previous_second = 0

def count_time():
    global previous_second, seconds, minutes
    now = datetime.now()
    current_second = now.strftime("%S")
    if current_second != previous_second:
        previous_second = current_second
        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
            if minutes == 60:
                minutes = 0
    return seconds, minutes


