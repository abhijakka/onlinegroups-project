import re
s = '\n \t this is a string   with a lot of whitespace\t'
s = re.sub('\n+', '', s)