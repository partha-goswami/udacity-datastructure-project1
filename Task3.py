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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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
initiated_caller_code = "(080)"
fixed_line_start_char, fixed_line_end_char = "(", ")"
mobile_starting_number_list = ["7", "8", "9"]
telemarketing_area_code = "140"
mobile_number_middle_character = " "
mobile_number_length_with_middle_space = 11
blore_to_blore_count = 0


list_of_codes = []

if len(calls) > 0:
    for caller, receiver, time, duration in calls:
        if caller.startswith(initiated_caller_code) and len(receiver) > 0:

            # Fixed line case
            if receiver.startswith(fixed_line_start_char) and receiver.find(fixed_line_end_char) != -1:
                list_of_codes.append(receiver[receiver.find(fixed_line_start_char) + 1:receiver.find(fixed_line_end_char)])

                # Bangalore to Bangalore Calls
                if receiver.startswith(initiated_caller_code):
                    blore_to_blore_count += 1

            # Mobile number case
            elif receiver[0] in mobile_starting_number_list \
                    and len(receiver) == mobile_number_length_with_middle_space \
                    and receiver[5] == mobile_number_middle_character:
                list_of_codes.append(receiver[:4])

            # Telecaller case
            elif receiver.startswith(telemarketing_area_code):
                list_of_codes.append(receiver[:3])

if len(list_of_codes) > 0:
    total_calls_with_duplicates = len(list_of_codes)
    list_of_codes = list(set(list_of_codes))
    list_of_codes.sort()

    # Part A
    print("The numbers called by people in Bangalore have codes:")
    for code in list_of_codes:
        print(code, sep="\n")

    # Part B
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
          .format(round((blore_to_blore_count/total_calls_with_duplicates) * 100, 2)))