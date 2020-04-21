# A regular expression in a programming language is a special text string used for describing a search pattern. It is extremely useful for extracting information from text such as code, files, log, spreadsheets or even documents.

# While using the regular expression the first thing is to recognize is that everything is essentially a character, and we are writing patterns to match a specific sequence of characters also referred as string. Ascii or latin letters are those that are on your keyboards and Unicode is used to match the foreign text. It includes digits and punctuation and all special characters like $#@!%, etc.

import re

xx = "qodr, education is fun"
r1 = re.findall(r"^\w+",xx)
print(r1)
print((re.split(r'\s','we are splitting the words')))
print((re.split(r's','split the words')))

# using re.match()
list = ["guru get", "guru give", "guru selenium"]
for element in list:
    z = re.match("(g\w+)\W(g\w+)", element)
    if z:
        print((z.groups()))

# using re.search()
patterns = ['software testing', 'guru']
text = 'software testing is fun?'

for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')

    if re.search(pattern, text):
        print('found a match!')
    else:
        print('no match')

# using re.findall()
abc = 'guru@google.com, career@google.com, users@google.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)

for email in emails:
    print(email)

# Python Flags
xx =  """guru
career
selenium"""

k1 = re.findall(r"^\w", xx)
k2 = re.findall(r"^\w", xx, re.MULTILINE)
print(k1)
print(k2)
