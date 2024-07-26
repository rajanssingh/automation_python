import re

# Phone number regex patter - 333-333-4444

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObjs = re.search(phoneNumRegex, "My phone number is 111-222-3333. Its not 111-222-333")
print("Phone number found : " + matchObjs.group())
print("--------------------------------------------------------------------------------------")

#  Grouping with parenthesis eg (111)-(222-4444)
phoneNumRegex2 = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d)')
matchObjs2 = re.search(phoneNumRegex2, "My phone number is (111)-222-3333. Its not 111-222-3333")
print(matchObjs2.group(1))
print(matchObjs2.group(2))
areaCode, mainNumber = matchObjs2.groups()
print(areaCode)
print(mainNumber)
print("--------------------------------------------------------------------------------------")

#  Pipe symbol usage
#  Match any of the string 'Batman','Batmobile','Batcopter','Bat', all start with Bat
batRegex = re.compile(r'Bat(man|mobile|copter)')
matchObjs3 = batRegex.search('Batmobile lost a wheel, Batman fell, need Batcopter now, Bats are here')
print(matchObjs3.groups())
print(matchObjs3.group())
print("--------------------------------------------------------------------------------------")

#  Optional matching using '?'
# Pattern to match only optionally. '?' character flags the group preceding it as an optional part of the pattern.
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
mo2 = batRegex.search('The adventures of Batwoman')
print(mo1.group())
print(mo2.group())
# Phone numbers that do or donot have the area code in phone number
phoneNumRegex = re.compile(r'((\(\d\d\d\)))?-(\d\d\d-\d\d\d)')
mo1 = phoneNumRegex.search('(111)-222-333')
mo2 = phoneNumRegex.search('111-222-333')
mo3 = phoneNumRegex.search('()-222-333')

print(mo1.group() + " --> " + mo2.group() + " --> " + mo3.group())
print("--------------------------------------------------------------------------------------")

# Matching zero or more with the plus
# '*' - zero or more,  '+' - one or more
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1 is None)
mo1 = batRegex.search('The adventures of Batwoman')
print(mo1.group())
mo1 = batRegex.search('The adventures of Batwowowoman')
print(mo1.group())
# Matching specific repetitions using {}
haRegex = re.compile(r'(ha){3}')
mo1 = haRegex.search('hahaha')
print(mo1.group())
haRegex = re.compile(r'(ha){3,5}')
mo1 = haRegex.search('haha')
print(mo1 is None)
mo1 = haRegex.search('hahahahaha')
print(mo1.group())

# Greedy and non-greedy matching
greedyRegex = re.compile(r'(ha){3,5}')
nonGreedyRegex = re.compile(r'(ha){3,5}?')
print(greedyRegex.search('hahahahaha').group())
print(nonGreedyRegex.search('hahahahaha').group())
print("--------------------------------------------------------------------------------------")

# findall() method
batRegex = re.compile(r'Bat(man|mobile|copter)')
print(batRegex.findall('Batmobile lost a wheel, Batman fell, need Batcopter now, Bats are here'))
# If there are groups in regex, findall() will return list of tuples. Each tuple represents a found match
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)')
print(phoneNumRegex.findall('Home: 415-541-8588 Work: 022-222-3331'))

# Character class
# Number then one space then some string(may be empty)
regex = re.compile(r'\d+\s\w*')
print(regex.findall('10 mangoes 12 oranges 13 pineapples 14 cakes 15 '))
# Define your own character class using '[]'
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Hi My name IS Rajan Kumar Singh'))
print(re.compile(r'[a-zA-Z0-9]').findall('a d^n2'))
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Hi My name IS Rajan Kumar Singh'))