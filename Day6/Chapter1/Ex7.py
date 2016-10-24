import re
r=re.compile("ck+w")
print(r.search("ckw"))
print(r.search("ckkkkkkkw"))
print(r.search(("ckkkkkk")))
print(r.search("cw"))
