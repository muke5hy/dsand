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

def get_telephone_time(calls):
    total = {}
    for call in calls:
        if call[0] not in total:
            total[call[0]] = int(call[3])
        else:
            total[call[0]] += int(call[3])

        if call[1] not in total:
            total[call[1]] = int(call[3])
        else:
            total[call[1]] += int(call[3])

    telephone_final = ''
    max_time = 0
    for item in total:
        if max_time < total[item]:
            telephone_final = item
            max_time = total[item]

    print(f"{telephone_final} spent the longest time, {max_time} seconds, on the phone during September 2016.")
    
get_telephone_time(calls)