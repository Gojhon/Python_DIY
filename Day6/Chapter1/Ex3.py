import re
r=re.compile("[pP]")
print(r.search("apple"))
print(r.match("apple"))
print(r.match("apPle"))
print(r.match("pP"))