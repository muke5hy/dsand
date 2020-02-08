"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from datetime import datetime
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def get_date_time_from_str(string: str) -> datetime :
    return datetime.strptime(texts[0][2], '%d-%m-%Y %H:%M:%S')
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

if __name__ == "__main__":    
    # get first record and print
    date = get_date_time_from_str(texts[0][2])
    print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time {date.time()}")

    # get second record and print
    date = get_date_time_from_str(calls[-1][2])
    print(f"Last record of calls, {calls[-1][0]} calls {calls[-1][1]} at time {date.time()}, lasting {date.time().second} seconds")