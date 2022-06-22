"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def get_telephone_with_prefix(calls: list) -> list:
    caller = set()
    reciever = set()
    for call in calls:
        caller.add(call[0])
        reciever.add(call[1])
    return list(caller), list(reciever)


caller, reciever = get_telephone_with_prefix(calls)
texter, reciever_txt = get_telephone_with_prefix(texts)

unique_no = list(set(reciever + texter+reciever_txt))
telemarketer = []
for n in caller:
    if n not in unique_no:
        telemarketer.append(n)
        
print("These numbers could be telemarketers: ")
for tel in sorted(telemarketer):
    print(tel)