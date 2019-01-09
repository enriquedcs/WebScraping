import re


# re.compile(pattern)    -- returns a regex object

regex = re.compile('[^a-hA-Z]')

# regex.match(string to match) --- returns Non if no match else a match object

print(regex.match('1'))

