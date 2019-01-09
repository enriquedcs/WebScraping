import re


# * character - this specifies that the previous character can be matched zero or more times, instead of exactly once.

#regex = re.compile('[a-c]*')     # lower limit us 0 and the upper limit is infinity

#print(regex.match('aaaaaaaaaaaaaaaaaa'))


# difference from * -- 0 - infinity    + 1 - infinity

regex = re.compile('a+')

print(regex.match('aaaaaaaaaaaa'))

# using character classes

regex = re.compile('[a-c]*')

print(regex.match(' '))