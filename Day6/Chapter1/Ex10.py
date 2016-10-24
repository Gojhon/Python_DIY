import re
r=re.compile("[abcd]")
print(r.search("pizza"))
print(r.search("bread"))
print(r.search("mashroom"))