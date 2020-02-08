"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def get_telephone_with_prefix(calls: list) -> list:
    caller = set()
    reciever = set()
    for call in calls:
        caller.add(call[0])
        reciever.add(call[1])
    return caller, reciever

def get_codes(numbers : set) -> list:
    codes = set()
    for number in numbers:
        phone = re.search(r'\((.*?)\)',number)
        if phone:
            codes.add(phone.group(1))
        elif number.startswith('140'):
            codes.add('140')
        elif number.startswith(('7','8','9')) and ' ' in number:
            codes.add(number[:4])
      
    print("The numbers called by people in Bangalore have codes:")
    for code in sorted(codes):
        print(code)

def get_percentage(callers: list, recievers: list) -> None:
    total = 0
    both = 0
    for caller, reciever in zip(callers, recievers):
        if caller.startswith('(080)'):
            total += 1
            if reciever.startswith('(080)'):
                both += 1
    
    percentage = round((both*100)/total, 2)
    print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

caller, reciever = get_telephone_with_prefix(calls)
get_codes(caller)
get_percentage(caller, reciever)
