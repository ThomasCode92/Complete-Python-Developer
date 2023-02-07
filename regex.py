# Regular Expressions

# A regular expression (shortened as regex or regexp) is a sequence of characters
# that specifies a search pattern in text.

import re as regex

pattern = regex.compile('this')
string = 'search this inside of this text please!'

print('search' in string)

result = pattern.search(string)
print(result.span())

result = pattern.findall(string)
print(result)

result = pattern.fullmatch(string)
print(result)

result = pattern.match(string)
print(result)
