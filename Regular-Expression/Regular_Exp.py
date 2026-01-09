

print("=============Regular Expressions (Regex)===================")
# Regex is a pattern used to find, match, or replace text.


import re

result = re.match(r'hello', 'hello world')  # Match     Checks from beginning of string
# print(result)
result = re.match(r'world', 'hello world')  # No match


result = re.search(r'world', 'hello world')  # Match!  (Searches anywhere in string)


matches = re.finditer(r'\d+', 'I have 2 apples and 5 oranges')   # ['2', '5'] -- (Finds ALL matches)
# print(matches)

# re.finditer()
matches = re.finditer(r'\d+', 'I have 2 apples and 5 oranges')   # ['2', '5'] -- (returns iterators)
for match in matches:
    # print(match.span())
    print(match.group(), match.span())          # 2- match, (7, 8) - span(start, end)

# re.sub()
text = re.sub(r'\d+', '#', 'I have 2 apples and 5 oranges')     # Replace patterns
# I have # apples and # oranges

# re.compile() - Pre-compile pattern for reuse
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
result = pattern.search('Call 123-456-7890 now!')
# print(result)           # 123-456-7890

print("================Second example==========================")



with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()



# Extract all usernames
username = re.findall(r"Username: [a-zA-Z0-9._]+", content)
print(username)     # ['Username: ade_ogun23', 'Username: fatima_musa', 'Username: dave_okeke99']


# Extract all emails
emails = re.findall(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9-.]+\.[a-zA-Z]{1,}", content)
print(emails)


# Extract all phone numbers
# phonenum = re.findall(r"\+?234\s?\d{10}", content)
phonenum = re.findall(r"Phone: \+?234\s?\d+", content)
print(phonenum)


# Extract all prices
price = re.findall(r"₦\d{1,}\,\d{3}\.\d{2}", content)
print(price)            # ['₦125,500.75', '₦87,250.00', '₦45,000.50']


# Extract all account numbers
acctnum = re.findall(r"Account No: \d{10}", content)
print(acctnum)      # ['Account No: 4500987612', 'Account No: 7823459901', 'Account No: 9900123456']


# Extract all registration dates
pattern = re.compile(r"Registered: \d{1,}[/-]\d{2}[/-]\d{4}")
regdate = pattern.findall(content)
print(regdate)  # ['Registered: 05-03-2022', 'Registered: 19-11-2023', 'Registered: 1/01/2024']


# Extract all transaction IDs
pattern = re.compile(r"TXN-[a-zA-Z0-9]+")
Transactions = pattern.findall(content)
print(Transactions)     # ['TXN-001234', 'TXN-998877', 'TXN-445566', 'TXN-ABC123']


# Replace all balances with ₦***
replac_blance = re.sub(r"₦\d{1,3}\,\d{3}\.\d{2}", "₦***", content)
# print(replac_blance)




print("==================Validate inputs=====================")

import re

# Validate a PIN (4 digits)
def valid_pin(pin):
    return bool(re.fullmatch(r"\d{4}", pin))       # Must be exactly 4 digits - ^\d{4}$

print(valid_pin("1234"))   # True
print(valid_pin("12a4"))   # False
print(valid_pin("12345"))  # False


print("=======================================")
# Validate Nigerian Phone Number
# Must start with 0 and must be 11 digits -- ^0\d{10}$

def valid_phone(phone):
    return bool(re.fullmatch(r"0\d{10}", phone))

print(valid_phone("08123456789"))  # True
print(valid_phone("9012345678"))   # False


print("=======================================")
# Validate Email: letters/numbers before @, valid domain, dot extension
def valid_email(email):
    return bool(re.fullmatch(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email))


print("=======================================")
# Validate Password (Strong)
# At least 8 characters, 1 uppercase, 1 lowercase, 1 digit, 1 special character
def strong_password(password):
    pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}"
    return bool(re.fullmatch(pattern, password))


print(strong_password('katstTEE$39$'))

print("==================Symbol & Meaning========================")
# Symbol	Meaning
# .	        Any character
# \.        Matches only .
# ^	        Start of string
# $	        End of string
# *	        0 or more
# +	        1 or more
# ?	        0 or 1 
# s?        optional s
# (?=...)   check condition - Look ahead and check if.. (?<=) lookbehind
# (?!)
# -         Specify a range of numbers [1-5]
# |         Either Or
# []	    Character set
# [^ ]      Matches Characters NOT in brackets
# ()	    Grouping
# {n}       exactly n
# {n,}      n or more times
# {n,m}     Between n and m times
# \d        Digit (0-9)
# \D        Not a Digit (0-9)
# \w        Word Character [A-Za-z0-9_]
# \W        Not a Word Character
# \s        Whitespace (space, tab, newline)
# \S        Not Whitespace (space, tab, newline)
# \b        Word Boundary
# \B        Not a Word Boundary
# search    First match anywhere  (search one object)
# findall   All matches (strings) (return a list)
# finditer  All matches (objects)   (return iterable and shows its index)
# sub       Replace
# compile   Reusable pattern
# match     Match at start (match at the begining of a string)
# re.fullmatch() # must match everything- used for validation

# (abc)     Capturing group
# \1, \2    Backreferences to captured groups
# Flags.I   (r'start', re.I)    (IGNORECASE SENSITIVE SEARCH FOR start)
# re.g         Global (all matches)


# m.group()   # matched text
# m.start()   # start index
# m.end()     # end index
# m.span()    # (start, end) indexs

