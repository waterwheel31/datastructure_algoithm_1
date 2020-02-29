"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

tel_number = ""
max_time = 0
total_time = {}

for call in calls: 
    time = int(call[3])
    phone1 = call[0]
    phone2 = call[1]
    try: total_time[phone1] += time
    except: total_time[phone1] = time

    try: total_time[phone2] += time
    except: total_time[phone2] = time

    if total_time[phone1] > max_time:
        max_time = total_time[phone1]
        tel_number = phone1

    if total_time[phone2] > max_time:
        max_time = total_time[phone2]
        tel_number = phone2

print("{}spent the longest time,{} seconds, on the phone during".format(tel_number, max_time) )

