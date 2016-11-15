import re
r=re.compile("a.c")
print(r.search("abc"))
print(r.search("afc"))
print(r.search("ac"))