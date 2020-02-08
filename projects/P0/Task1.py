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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def get_telephone_number(data):
    mobile = []
    for item in data:
        mobile.append(item[0])
        mobile.append(item[1])

    return mobile

if __name__ == "__main__":    
    telephone = get_telephone_number(texts) + get_telephone_number(calls)

    unique_telephone_number = list(set(telephone))
    total = len(unique_telephone_number)

    print(f"There are {total} different telephone numbers in the records.")