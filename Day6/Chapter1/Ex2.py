import re
r=re.compile("[ab]")
print(r.search("pizza"))
print(r.match("pizza"))